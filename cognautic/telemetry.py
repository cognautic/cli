import requests
import threading
import json
import time
import os
from dotenv import load_dotenv

# Load from .env file if it exists
load_dotenv()

class TelemetryClient:
    def __init__(self, supabase_url=None, supabase_anon_key=None, enabled=True):
        self.supabase_url = supabase_url or os.getenv("NEXT_PUBLIC_SUPABASE_URL")
        self.supabase_anon_key = supabase_anon_key or os.getenv("NEXT_PUBLIC_SUPABASE_ANON_KEY")
        self.enabled = enabled and bool(self.supabase_url and self.supabase_anon_key)
        
        if self.enabled:
            self.url = f"{self.supabase_url}/rest/v1/events"
            self.headers = {
                "apikey": self.supabase_anon_key,
                "Authorization": f"Bearer {self.supabase_anon_key}",
                "Content-Type": "application/json",
                "Prefer": "return=minimal"
            }

    def track_event(self, product, event, version=None, user_id=None, platform=None, meta=None):
        if not self.enabled:
            return

        data = {
            "product": product,
            "event": event,
            "version": version,
            "user_id": user_id,
            "platform": platform,
            "meta": meta,
        }

        # Run in background thread to be non-blocking
        threading.Thread(target=self._send_event, args=(data,), daemon=True).start()

    def _send_event(self, data, attempt=0):
        try:
            response = requests.post(self.url, headers=self.headers, json=data, timeout=5)
            response.raise_for_status()
        except Exception:
            if attempt < 2:
                time.sleep(1 * (attempt + 1))
                self._send_event(data, attempt + 1)
