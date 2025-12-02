"""
Repository Documenter for Cognautic CLI
Generates comprehensive documentation for public git repositories using AI
"""

import os
import shutil
from pathlib import Path
from rich.console import Console

console = Console()


async def document_repository(repo_url: str, workspace: str, ai_engine, provider: str, model: str, memory_manager=None) -> bool:
    """
    Document a git repository by cloning it and asking AI to analyze it
    
    Args:
        repo_url: URL of the git repository
        workspace: Current workspace directory
        ai_engine: AI engine instance for generating documentation
        provider: AI provider to use
        model: AI model to use
        memory_manager: Memory manager for conversation context
        
    Returns:
        True if successful, False otherwise
    """
    console.print(f"Analyzing repository: {repo_url}...", style="cyan")
    
    # Extract repo name from URL
    repo_name = repo_url.split('/')[-1].replace('.git', '')
    
    # Create tmp directory in workspace
    tmp_base = Path(workspace) / "tmp"
    
    try:
        tmp_base.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        console.print(f"Error creating tmp directory: {e}", style="red")
        return False
    
    repo_dir = tmp_base / repo_name
    console.print(f"Cloning to: {repo_dir}", style="dim")
    
    # Clean up existing directory if needed
    if repo_dir.exists():
        console.print(f"Removing existing directory...", style="dim")
        try:
            if repo_dir.is_dir():
                shutil.rmtree(repo_dir)
            else:
                repo_dir.unlink()
        except Exception as e:
            console.print(f"Error cleaning up existing dir: {e}", style="red")
            return False
    
    # Clone repository
    console.print("Cloning repository...", style="dim")
    import subprocess
    
    try:
        result = subprocess.run(
            f"git clone --depth 1 {repo_url} {repo_dir}",
            shell=True,
            capture_output=True,
            text=True,
            timeout=60
        )
        
        if result.returncode != 0:
            console.print(f"Error cloning repo: {result.stderr}", style="red")
            if "Authentication failed" in result.stderr:
                console.print("Please ensure the repository is public.", style="yellow")
            return False
    except subprocess.TimeoutExpired:
        console.print("Error: Clone operation timed out", style="red")
        return False
    except Exception as e:
        console.print(f"Error executing git clone: {e}", style="red")
        return False
    
    if not repo_dir.exists() or not any(repo_dir.iterdir()):
        console.print("Error: Repository directory is empty after clone.", style="red")
        return False
    
    # Analyze file structure
    console.print("Analyzing file structure...", style="dim")
    file_structure = []
    file_contents = {}
    
    # Walk through the repository
    for root, dirs, files in os.walk(repo_dir):
        # Skip .git directories
        if '.git' in dirs:
            dirs.remove('.git')
        
        rel_path = os.path.relpath(root, repo_dir)
        if rel_path == ".":
            rel_path = ""
        
        for file in files:
            # Skip hidden files
            if file.startswith('.'):
                continue
            
            full_path = os.path.join(root, file)
            file_path = os.path.join(rel_path, file) if rel_path else file
            file_structure.append(file_path)
            
            # Read key configuration files
            if file.lower() in ['readme.md', 'package.json', 'requirements.txt', 
                               'cargo.toml', 'go.mod', 'pom.xml', 'build.gradle',
                               'setup.py', 'pyproject.toml', 'composer.json']:
                try:
                    with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                        file_contents[file_path] = f.read()
                except Exception:
                    pass
            
            # Read source files (limit size to avoid context overflow)
            elif file.endswith(('.py', '.js', '.ts', '.tsx', '.jsx', '.rs', '.go', 
                               '.java', '.c', '.cpp', '.h', '.rb', '.php', '.vue',
                               '.swift', '.kt', '.scala', '.cs')):
                try:
                    file_size = os.path.getsize(full_path)
                    if file_size < 15000:  # Less than 15KB
                        with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                            file_contents[file_path] = f.read()
                except Exception:
                    pass
    
    if not file_structure:
        console.print("Warning: No files found in the repository.", style="yellow")
    else:
        console.print(f"Found {len(file_structure)} files.", style="dim")
    
    # Construct user message for AI
    user_message = f"""Please analyze the following git repository and create comprehensive documentation for it.

Repository: {repo_url}
Repository Name: {repo_name}

File Structure (First 300 files):
```
{chr(10).join(file_structure[:300])}
{'(... truncated)' if len(file_structure) > 300 else ''}
```

Key File Contents:
"""
    
    # Limit total content to avoid token limits
    total_chars = 0
    max_chars = 50000
    
    for path, content in file_contents.items():
        if total_chars > max_chars:
            user_message += "\n\n(Remaining file contents truncated due to size limits...)\n"
            break
        
        snippet = content[:3000]  # Limit per file
        user_message += f"\n--- {path} ---\n```\n{snippet}\n```\n"
        total_chars += len(snippet)
    
    user_message += f"""

Please create the following files using your file creation tools:

1. **{repo_name}_DOCS.md** - A comprehensive documentation file including:
   - Project Overview: What is this project?
   - Installation: How to install/setup
   - Usage: How to use it
   - Code Structure: Explanation of the directory structure and key modules
   - Architecture: A brief text description of the architecture

2. **extra/{repo_name}_graph.py** - A Python script using the `graphviz` library to generate a high-quality architecture diagram of this project. The script must be self-contained and runnable.

Please use your write_to_file tool to create these files. Do NOT just output the content - actually create the files.
"""
    
    console.print(f"Sending analysis request to AI ({len(user_message)} chars)...", style="cyan")
    
    # Get conversation history if available
    conversation_history = []
    if memory_manager:
        conversation_history = memory_manager.get_context_for_ai(limit=5)
    
    # Send message to AI and let it use tools to create files
    try:
        console.print("\n[bold cyan]AI is analyzing the repository and creating documentation...[/bold cyan]\n")
        
        response = ""
        async for chunk in ai_engine.process_message_stream(
            user_message,
            provider=provider,
            model=model,
            project_path=workspace,
            conversation_history=conversation_history
        ):
            response += chunk
        
        # Clean up cloned repository
        try:
            console.print("\n[dim]Cleaning up temporary files...[/dim]")
            shutil.rmtree(repo_dir)
        except Exception as e:
            console.print(f"[yellow]Warning: Could not clean up temp directory: {e}[/yellow]")
        
        console.print("\n[bold green]✓ Repository documentation complete![/bold green]")
        console.print(f"[green]The AI has created the documentation files in your workspace.[/green]")
        
        return True
        
    except Exception as e:
        console.print(f"Error during AI analysis: {e}", style="red")
        
        # Clean up on error
        try:
            if repo_dir.exists():
                shutil.rmtree(repo_dir)
        except Exception:
            pass
        
        return False
