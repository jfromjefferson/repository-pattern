from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Film:
    film_id: Optional[int]
    title: str
    description: str
    release_year: int
    language_id: int
    rental_duration: int
    rental_rate: float
    length: int
    replacement_cost: float
    rating: str
    last_update: datetime
    special_features: str
    fulltext: str