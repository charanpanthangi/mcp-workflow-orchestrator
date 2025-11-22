"""Logging helpers for tracking orchestrator activity."""
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("workflow-orchestrator")
