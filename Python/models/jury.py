from abc import ABC
from dataclasses import field, dataclass
from typing import Optional


@dataclass
class Jury(ABC):
    """Groupe de personne qui se charge de voter le livre de son choix"""
    id_jury: Optional[int] = field(default=None, init=False)
    j_nom : str
    j_role : str | None
    def __str__(self) -> str:
        return f"Role jury :  {self.j_role}" + f"Nom Jury {self.j_nom}"