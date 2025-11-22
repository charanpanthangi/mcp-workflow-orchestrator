"""Simple JSON-based preference store for workflow memory."""
import json
import os
from typing import Dict, Any

from app.observability.logging_utils import logger

STORE_PATH = os.getenv("PREFERENCE_STORE_PATH", "memory_store.json")


class PreferenceStore:
    """Persist user preferences and past interactions to disk."""

    def __init__(self, path: str = STORE_PATH) -> None:
        self.path = path
        if not os.path.exists(self.path):
            self._write({"preferences": {}})

    def _write(self, data: Dict[str, Any]) -> None:
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def load_preferences(self) -> Dict[str, Any]:
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                data = json.load(f)
            return data.get("preferences", {})
        except FileNotFoundError:
            return {}

    def save_preferences(self, preferences: Dict[str, Any]) -> None:
        logger.debug("Persisting preferences: %s", preferences)
        current = {"preferences": preferences}
        self._write(current)
