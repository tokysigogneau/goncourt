from abc import ABC
from dataclasses import field, dataclass
from typing import Optional


@dataclass
class PersonnagesPrincipaux(ABC):
    """Les personnages principaux d'un livre."""
    id_perso_p: Optional[int] = field(default=None, init=False)
    pp_nom : str

    def __str__(self) -> str:
        return f"Personnages principaux :  {self.pp_nom}"