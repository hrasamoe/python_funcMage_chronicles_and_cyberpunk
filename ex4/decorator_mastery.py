#! /usr/bin/env python3
import time
from collections.abc import Callable
from functools import wraps
from typing import Any


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Spell completed in {end_time - start_time:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable[..., Any]:
    def func_wraps(fun: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(fun)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = kwargs.get('power', args[0] if args else None)
            if power is not None and power >= min_power:
                return fun(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return func_wraps


def retry_spell(max_attempts: int
                ) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... (attempt {attempt}"
                          f"/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f'Successfully cast {spell_name} with {power} power'

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and name.replace(' ', '').isalpha()


if __name__ == "__main__":
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.101)
        return "Fireball cast!"
    result = fireball()
    print(f"Result: {result}")

    @power_validator(10)
    def cast_lightning(power: int, target: str) -> str:
        return f'Successfully cast {target} with {power} power'
    print("\nTesting retrying spell...")

    @retry_spell(3)
    def cast_lightning_bolt(target: str) -> str:
        import random
        if random.random() > 0.5:
            raise RuntimeError("The mana stream was interrupted!")
        return f"Lightning bolt hits {target}!"
    print(cast_lightning_bolt())
    print('\nTesting MageGuild...')
    guild = MageGuild()
    print(guild.validate_mage_name('Ligh3tning'))
    print(guild.validate_mage_name('Fireball'))
    print(cast_lightning(power=15, target='Lightning'))
    print(cast_lightning(power=5, target='Dragon'))
