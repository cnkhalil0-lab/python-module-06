def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    # TECHNIQUE A : L'import local !
    # On importe le validateur uniquement au moment de lancer le sort.
    from .light_validator import validate_ingredients

    validation = validate_ingredients(ingredients)
    return f"Spell recorded: {spell_name} ({validation})"
