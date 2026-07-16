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
