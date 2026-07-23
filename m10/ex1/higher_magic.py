from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list[Callable]:
        return [spell(target, power) for spell in spells]
    return sequence


if __name__ == "__main__":

    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power} HP"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    print("Testing spell combiner...")

    combined = spell_combiner(fireball, heal)
    result = combined("Dragon", 10)

    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("\nTesting power amplifier...")

    original = fireball("Dragon", 10)
    amplified_spell = power_amplifier(fireball, 3)
    amplified = amplified_spell("Dragon", 10)

    print("This is an amplified attack:", amplified)
