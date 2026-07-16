#! /usr/bin/env python3
from typing import Callable


def spell_combiner(
    spell1: Callable[[str, int], str],
    spell2: Callable[[str, int], str]
) -> Callable[[str, int], tuple[str, str]]:
    def combiner(target: str, power: int) -> tuple[str, str]:
        result1 = spell1(target, power)
        result2 = spell2(target, power)
        return (result1, result2)
    return combiner


def power_amplifier(
    base_spell: Callable[[str, int], str],
    multiplier: int
) -> Callable[[str, int], str]:
    def amplifier(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplifier


def conditional_caster(
    condition: Callable[[str, int], bool],
    spell: Callable[[str, int], str]
) -> Callable[[str, int], str]:
    def caster(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spel fizzled"
    return caster


def spell_sequence(
        spells: Callable[[str, int], str]) -> Callable[[str, int], list[str]]:
    def cast_spell(target: str, power: int) -> list[str]:
        result = []
        for _ in spells:
            result.append(_(target, power))
        return result
    return cast_spell


if __name__ == "__main__":
    test_values = [12, 16, 13, 10]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    def heal(target: str, power: int) -> str:
        return f"Heals {target}"

    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target}"

    def displayPower(target: str, power: int) -> str:
        return f"{power}"

    def is_dragon(target: str, power: int) -> str:
        return target == "Dragon"

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined(test_targets[0], test_values[0])
    print(f'Combined spell result: {result[0]}, {result[1]}\n')
    print("Testing power amplifier...")
    amplifier = power_amplifier(displayPower, 3)
    result = amplifier(test_targets[1], test_values[3])
    print(f"Original: {displayPower(test_targets[1], test_values[3])},"
          f" Amplified: {result}")
