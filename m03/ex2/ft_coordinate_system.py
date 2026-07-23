import math


def get_player_pos() -> None:
    while True:
        user_input = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )

        parts = user_input.split(',')

        if len(parts) != 3:
            print("Invalid syntax")
            continue

        try:
            x = float(parts[0].strip())
            y = float(parts[1].strip())
            z = float(parts[2].strip())
            return (x, y, z)
        except ValueError:
            for i, part in enumerate(parts):
                try:
                    float(part.strip())
                except ValueError:
                    coord_name = ['x', 'y', 'z'][i]
                    print(f"Error on parameter '{coord_name}': "
                          "could not convert string to float: "
                          f"'{part.strip()}'")
                    break
            continue


def calculate_distance(point1: int, point2: int) -> int:
    x1, y1, z1 = point1
    x2, y2, z2 = point2

    distance = math.sqrt(
        (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2
    )
    return distance


def main():
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    first_pos = get_player_pos()

    print(f"Got a first tuple: {first_pos}")

    x, y, z = first_pos
    print(f"It includes: X={x}, Y={y}, Z={z}")

    center = (0.0, 0.0, 0.0)
    distance_to_center = calculate_distance(first_pos, center)

    print(f"Distance to center: {distance_to_center:.4f}")

    print("Get a second set of coordinates")
    second_pos = get_player_pos()

    distance_between = calculate_distance(first_pos, second_pos)

    print(f"Distance between the 2 sets of coordinates: "
          f"{distance_between:.4f}")


if __name__ == "__main__":
    main()
