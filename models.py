from dataclasses import dataclass
from datetime import datetime


@dataclass
class EVARecord:
    date: datetime
    duration_hours: float
    country: str
    crew: str
