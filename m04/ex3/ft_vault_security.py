def secure_archive(
    filename: str,
    mode: str = "read",
    content: str = ""
) -> tuple[bool, str]:
    try:
        if mode == "read":
            with open(filename, "r") as file:
                data = file.read()
            return True, data

        if mode == "write":
            with open(filename, "w") as file:
                file.write(content)
            return True, "Content successfully written to file"

        return False, "Invalid mode"

    except Exception as e:
        return False, str(e)


def main() -> None:
    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/passwd"))

    print("\nUsing 'secure_archive' to read from a regular file:")

    with open("fragment.txt", "w") as f:
        f.write(
            "[FRAGMENT 001] Digital preservation protocols established 2087\n"
            "[FRAGMENT 002] Knowledge must survive the entropy wars\n"
            "[FRAGMENT 003] Every byte saved is a victory against oblivion\n"
        )

    result = secure_archive("fragment.txt")
    print(result)

    print("\nUsing 'secure_archive' to write previous content to a new file:")

    success, data = result
    if success:
        print(secure_archive("new_fragment.txt", "write", data))


if __name__ == "__main__":
    main()
