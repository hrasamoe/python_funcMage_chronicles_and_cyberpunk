#! /usr/bin/env python3

from functools import reduce, lru_cache, singledispatch, partial
from typing import Any
from operator import add, mul
from collections.abc import Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    operations: dict[str, Callable[[int, int], int]] = {
        'add': add,
        'multiply': mul,
        'max': max,
        'min': min,
    }
    if operation not in operations:
        print(f"-- Operation <<{operation}>> is Unknown")
        return -1
    return reduce(operations[operation], spells)


def partial_enchanter(
    base_enchantment: Callable[..., str]
) -> dict[str, Callable[..., str]]:
    return {
        'fire': partial(base_enchantment, power=50, element="fire"),
        'ice': partial(base_enchantment, power=50, element="ice"),
        'thunder': partial(base_enchantment, power=50, element="thunder")
    }


@lru_cache(maxsize=30)
def memoized_fibonacci(n: int) -> int:
    try:
        if n < 0:
            raise ValueError('n must be a non-negative integer')
        if n <= 1:
            return n
        return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)
    except ValueError as e:
        print(f"Fibonacci error: {e}")
        return -1


def spell_dispatcher() -> Callable[[Any], str]:

    @singledispatch
    def spell_system(value: Any) -> str:
        return "Unknown spell type"

    @spell_system.register
    def _(value: str) -> str:
        return f"Enchantment: {value}"

    @spell_system.register
    def _(value: list[Any]) -> str:
        return f"Multi-cast: {len(value)} spells"

    @spell_system.register
    def _(value: int) -> str:
        return f"Damage spell: {value} damage"

    return spell_system


if __name__ == "__main__":
    list_spells = [10, 20, 30, 40]
    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer(list_spells, 'add')}")
    print(f"Product: {spell_reducer(list_spells, 'multiply')}")
    print(f"Max: {spell_reducer(list_spells, 'max')}\n")
    print("Testing memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}\n")
    print("Testing spell dispatcher...")
    spell = spell_dispatcher()
    print(spell(42))
    print(spell('fireball'))
    print(spell([10, 20, 30]))
    print(spell(3.14))
