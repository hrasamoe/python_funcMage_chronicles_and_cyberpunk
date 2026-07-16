#! /usr/bin/env python3

from typing import Callable


def mage_counter() -> Callable[[], int]:
    count = 0

    def increment_counter() -> int:
        nonlocal count
        count += 1
        return count
    return increment_counter


def spell_accumulator(intial_power: int) -> Callable[[int], int]:
    total_power = intial_power

    def increment_power(power: int) -> int:
        nonlocal total_power
        total_power += power
        return total_power
    return increment_power


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def factory(item_name: str) -> str:
        return f'{enchantment_type} {item_name}'
    return factory


def memory_vault() -> dict[str, Callable[..., object]]:
    vault = {}

    def store(key: str, value: object) -> None:
        vault[key] = value

    def recall(key: str) -> object:
        return vault.get(key, 'Memory not found')

    return {'store': store, 'recall': recall}


if __name__ == "__main__":
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")
    print()

    print("Testing spell accumulator...")
    accumulator = spell_accumulator(100)
    print(f"Base 100, add 20: {accumulator(20)}")
    print(f"Base 100, add 20: {accumulator(30)}")
    print()

    print("Tesint enchantment factory...")
    flaming = enchantment_factory('Flaming')
    frozen = enchantment_factory('Frozen')
    print(flaming('Sword'))
    print(frozen('Shield'))
    print()

    print("Testing memory vault...")
    vault = memory_vault()
    store = vault['store']
    recall = vault['recall']
    print("Store 'secret' = 42")
    store('secret', 42)
    print(f"Recall 'secret': {recall('secret')}")
    print(f"Recall 'unknown': {recall('unkown')}")
