from dataclasses import field, dataclass
from typing import Optional
from models.livre import  Livre


@dataclass
class Editeur:
    """Editeur qui publie le livre, il contient le nom de l'éditeur."""
    id_editeur: Optional[int] = field(default=None, init=False)
    e_nom : str

    def __str__(self) -> str:
        return f"Editeur :  {self.e_nom}"