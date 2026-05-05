import sys
from typing import TextIO


def print_content(f: TextIO) -> None:
    print("---")
    content: str = f.read()
    print(content, end="")
    print("---")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    print("=== Cyber Archives Recovery ===")

    filename: str = sys.argv[1]
    print(f"Accessing file '{filename}'")

    try:
        f: TextIO = open(filename, "r")

        print_content(f)

        f.close()
        print(f"File '{filename}' closed.")

    except Exception as e:
        print(f"Error opening file '{filename}': {e}")


if __name__ == "__main__":
    main()