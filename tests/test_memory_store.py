"""Tests for JSON-backed preference store."""
import os
from app.memory.store import PreferenceStore


def test_preference_store_roundtrip(tmp_path):
    path = tmp_path / "prefs.json"
    store = PreferenceStore(str(path))
    prefs = {"theme": "dark"}
    store.save_preferences(prefs)
    loaded = store.load_preferences()
    assert loaded == prefs
    assert os.path.exists(path)
