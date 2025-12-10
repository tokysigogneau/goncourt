from abc import ABC
from dataclasses import field, dataclass
from typing import Optional


@dataclass
class Resultat(ABC):
    """Résultats des votes et chaque tour"""
    id_resultat: Optional[int] = field(default=None, init=False)
    numero_selection : int
    total_votes : int
    def __str__(self) -> str:
        return (f"Selection numero :  {self.numero_selection}" +
                (f" total de votes: {self.total_votes}" ))