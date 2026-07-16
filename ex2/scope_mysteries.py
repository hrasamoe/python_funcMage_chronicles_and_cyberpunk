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
