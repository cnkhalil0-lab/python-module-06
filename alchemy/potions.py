# On importe les éléments de la racine (au-dessus)
from elements import create_fire, create_water

# On importe les éléments du même dossier (avec le point '.')
from .elements import create_earth, create_air


def healing_potion() -> str:
    return f"Healing potion brewed with '{create_earth()}' and '{create_air()}'"


def strength_potion() -> str:
    return f"Strength potion brewed with '{create_fire()}' and '{create_water()}'"
