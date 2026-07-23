import sys
from typing import IO


def read_file(filename: str) -> list[str]:
    file: IO[str] = open(filename, "r")
    content: str = file.read()
    file.close()
    return content.splitlines()


def transform(lines: list[str]) -> list[str]:
    return [line + "#" for line in lines]


def display(lines: list[str]) -> None:
    print("---\n")
    for line in lines:
        print(line)
    print("\n---")


def save_file(filename: str, lines: list[str]) -> None:
    file: IO[str] = open(filename, "w")
    file.write("\n".join(lines))
    file.close()


def print_error(message: str) -> None:
    sys.stderr.write(f"[STDERR] {message}\n")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return

    filename: str = sys.argv[1]

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    try:
        lines: list[str] = read_file(filename)
    except Exception as e:
        print_error(f"Error opening file '{filename}': {e}")
        return

    display(lines)
    print(f"File '{filename}' closed.\n")

    transformed: list[str] = transform(lines)

    print("Transform data:")
    display(transformed)

    print("Enter new file name (or empty): ", end="")
    sys.stdout.flush()

    new_file: str = sys.stdin.readline().strip()

    if new_file == "":
        print("Data not saved.")
        return

    print(f"Saving data to '{new_file}'")

    try:
        save_file(new_file, transformed)
    except Exception as e:
        print_error(f"Error opening file '{new_file}': {e}")
        print("Data not saved.")
        return


if __name__ == "__main__":
    main()
