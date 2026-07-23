import time
from functools import wraps
from collections.abc import Callable
from typing import Any


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"Casting {func.__name__}...")

        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        duration = end - start
        print(f"Spell completed in {duration:.3f} seconds")

        return result

    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:

        @wraps(func)
        def wrapper(self, spell_name: str, power: int, *args, **kwargs) -> Any:
            if power <= min_power:
                return "Insufficient power for this spell"
            return func(self, spell_name, power, *args, **kwargs)

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:

        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            attempt = 1

            while attempt <= max_attempts:
                try:
                    return func(*args, **kwargs)

                except Exception:
                    if attempt == max_attempts:
                        return (
                            f"Spell casting failed after "
                            f"{max_attempts} attempts"
                        )

                    print(
                        "Spell failed, retrying... "
                        f"(attempt {attempt}/{max_attempts})"
                    )

                    attempt += 1

            return (
                f"Spell casting failed after "
                f"{max_attempts} attempts"
            )

        return wrapper

    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False

        return all(c.isalpha() or c == " " for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":

    print("Testing spell timer...")

    @spell_timer
    def fireball():
        time.sleep(0.101)
        return "Fireball cast!"

    result = fireball()
    print(f"Result: {result}")

    print("\nTesting retrying spell...")

    attempt_counter = {"count": 0}

    @retry_spell(3)
    def unstable_spell():
        raise ValueError("Magic overload")

    print(unstable_spell())

    print("\nTesting MageGuild...")

    guild = MageGuild()

    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("Al"))

    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Fireball", 5))
