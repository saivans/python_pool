def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if (unit == "packets"):
        print(f"{seed_type.capitalize()} seeds: {quantity} packets available")
    elif (unit == "grams"):
        print(f"{seed_type.capitalize()} seeds: {quantity} grams total")
    elif (unit == "area"):
        x = quantity
        print(f"{seed_type.capitalize()} seeds: covers {x} square meters")
    else:
        print("Unknown unit type")
