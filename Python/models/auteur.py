from dataclasses import field, dataclass
from typing import Optional

#Pour éviter les imports circulaires
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.livre import  Livre


@dataclass
class Auteur():
    """Auteur qui écrit le livre, il contient le nom de lauteur et une biographie facultative."""
    id_auteur: Optional[int] = field(default=None, init=False)
    a_nom : str
    a_biographie : str | None
    def __str__(self) -> str:
        return f"Auteur :  {self.a_nom}" +\
            (f", {self.a_biographie}" if self.a_biographie is not None else '')