"""Preference schema for memory persistence."""
from typing import Dict, Any
from pydantic import BaseModel


class PreferenceRecord(BaseModel):
    """Represents stored user preferences."""

    preferences: Dict[str, Any]
