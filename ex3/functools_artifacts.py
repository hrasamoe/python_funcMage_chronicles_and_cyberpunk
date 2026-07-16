#! /usr/bin/env python3

from functools import reduce, lru_cache, singledispatch, partial
from typing import Callable
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    try:
        if operation == 'add':
            return reduce(add, spells)
        elif operation == 'multiply':
            return reduce(mul, spells)
        elif operation == 'max':
            return reduce(max, spells)
        elif operation == 'min':
            return reduce(min, spells)
        else:
            raise TypeError
    except TypeError as e:
        print(f"-- Operation <<{operation}>> is Unkown {e}")
        return -1


def partial_enchanter(
        base_enchantment: Callable[..., str]) -> dict[str, Callable[..., str]]:
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


def spell_dispatcher() -> Callable[[any], str]:

    @singledispatch
    def spell_system(value: any) -> str:
        return "Unknown spell type"

    @spell_system.register
    def _(value: str) -> str:
        return f"Enchantment: {value}"

    @spell_system.register
    def _(value: list) -> str:
        return f"Multi-cast: {len(value)} spells"

    @spell_system.register
    def _(value: int) -> str:
        return f"Damage spell: {value} damage"

    return spell_system
