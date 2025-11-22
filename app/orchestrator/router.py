"""Agent router mapping agent names to concrete implementations."""
from typing import Dict, Type

from app.agents.base_agent import BaseAgent
from app.agents.weather_agent import WeatherAgent
from app.agents.budget_agent import BudgetAgent
from app.agents.calendar_agent import CalendarAgent
from app.agents.visa_agent import VisaAgent
from app.agents.flight_agent import FlightAgent
from app.agents.hotel_agent import HotelAgent
from app.agents.taxi_agent import TaxiAgent
from app.agents.response_agent import ResponseAgent

# Registry used by the planner to look up agent classes by identifier.
AGENT_REGISTRY: Dict[str, Type[BaseAgent]] = {
    "weather": WeatherAgent,
    "budget": BudgetAgent,
    "calendar": CalendarAgent,
    "visa": VisaAgent,
    "flight": FlightAgent,
    "hotel": HotelAgent,
    "taxi": TaxiAgent,
    "response": ResponseAgent,
}


def get_agent_class(name: str) -> Type[BaseAgent]:
    """Return the agent class for a given identifier, raising for unknown."""
    if name not in AGENT_REGISTRY:
        raise ValueError(f"Unknown agent requested: {name}")
    return AGENT_REGISTRY[name]
