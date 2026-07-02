from dataclasses import dataclass
from typing import Optional

@dataclass
class Job:
    company: str
    role: str
    location: str
    apply_link: str
    source: str
    posted_date: Optional[str] = None
    salary: Optional[str] = None
    experience: Optional[str] = None
    description: Optional[str] = None
    score: float = 0.0
    status: str = "Pending"