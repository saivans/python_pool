import sys
from typing import Dict, List


def parse_arguments() -> Dict[str, int]:
    inventory: Dict[str, int] = {}

    print("=== Inventory System Analysis ===")

    for arg in sys.argv[1:]:
        if ':' not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue

        parts: List[str] = arg.split(':', 1)
        item_name: str = parts[0]
        quantity_str: str = parts[1]

        if item_name in inventory:
            print(f"Redundant item '{item_name}' - discarding")
            continue

        try:
            quantity: int = int(quantity_str)
            inventory[item_name] = quantity
        except ValueError:
            print(f"Quantity error for '{item_name}': "
                  f"invalid literal for int() with base 10: '{quantity_str}'")

    return inventory


def display_inventory(inventory: Dict[str, int]) -> None:
    print(f"Got inventory: {inventory}")


def display_item_list(inventory: Dict[str, int]) -> None:
    items: List[str] = list(inventory.keys())
    print(f"Item list: {items}")


def display_total_quantity(inventory: Dict[str, int]) -> None:
    total: int = sum(inventory.values())
    count: int = len(inventory)
    print(f"Total quantity of the {count} items: {total}")


def display_percentages(inventory: Dict[str, int]) -> None:
    total: int = sum(inventory.values())

    for item, quantity in inventory.items():
        percentage: float = (quantity / total) * 100
        print(f"Item {item} represents {percentage:.1f}%")


def display_extremes(inventory: Dict[str, int]) -> None:
    if not inventory:
        return

    most_abundant: str = max(inventory.items(), key=lambda x: x[1])[0]
    least_abundant: str = min(inventory.items(), key=lambda x: x[1])[0]

    print(f"Item most abundant: {most_abundant} with quantity "
          f"{inventory[most_abundant]}")
    print(f"Item least abundant: {least_abundant} with quantity "
          f"{inventory[least_abundant]}")


def add_new_item(inventory: Dict[str, int]) -> None:
    inventory['magic_item'] = 1
    print(f"Updated inventory: {inventory}")


def main() -> None:
    inventory: Dict[str, int] = parse_arguments()

    display_inventory(inventory)
    display_item_list(inventory)
    display_total_quantity(inventory)
    display_percentages(inventory)
    display_extremes(inventory)
    add_new_item(inventory)


if __name__ == "__main__":
    main()
