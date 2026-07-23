#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")

    if len(sys.argv) == 1:
        print("No arguments provided!")
    else:
        num_args = len(sys.argv) - 1
        print(f"Arguments received: {num_args}")
        i = 1
        while i <= num_args:
            print("Argument", i, ":", sys.argv[i])
            i += 1

    print(f"Total arguments: {len(sys.argv)}")
