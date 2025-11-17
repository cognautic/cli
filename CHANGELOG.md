# Changelog

All notable changes to Cognautic CLI will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

All notable changes to this project will be documented in this file.

## [1.1.8] - 2025-11-17
- **Fixed**: Added short `-v` flag to print version and exit, alongside `--version`.
- **Fixed**: Resolved Click error handling crash when printing usage/errors by making the stderr filter a proper file-like proxy, avoiding "AttributeError: 'str' object has no attribute 'write'".
- **Improved**: Version reporting now sources from package `__version__`.
- **Added**: `@`-prefixed file path suggestions in chat prompt. Workspace-aware, supports relative, absolute, and `~` paths. Directories show with trailing `/` and expand.
- **Improved**: Tab now accepts the highlighted suggestion; Up/Down arrows navigate the completion list; Enter still sends the message.
- **Fixed**: Resolved `UnboundLocalError` for `Path` when using `/workspace` or `/ws` by removing an inner import that shadowed the module-level `Path`.
- **Compatibility**: Updated type hints to use `Optional[str]` for Python 3.8 support.

