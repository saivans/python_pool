def input_temperature(temp_str):
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print("")

    test_inputs = ["25", "abc"]

    for temp in test_inputs:
        print(f"Input data is '{temp}'")
        try:
            temperature = input_temperature(temp)
            print(f"Temperature is now {temperature}°C")
        except Exception as e:
            print(f"Caught input_temperature error: {e}")
        print("")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
