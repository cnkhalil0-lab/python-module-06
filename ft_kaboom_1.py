print("=== Kaboom 1 ===")
print("Access to alchemy/grimoire/dark_spellbook.py directly")
print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")


from alchemy.grimoire.dark_spellbook import dark_spell_record

# Le code n'arrivera jamais ici, le labo aura explosé avant.
print(f"Testing dark spell: {dark_spell_record('Curse', 'bats, frogs')}")
