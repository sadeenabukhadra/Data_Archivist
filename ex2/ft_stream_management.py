import sys
import typing


def print_content(f1: typing.IO) -> None:
    print("---")
    content: str = f1.read()
    print(content, end="")
    print("---")


def transform_data(f2: typing.IO) -> str:
    print("Transform data:")
    print("---")
    transformed: str = ""
    lines = f2.readlines()
    for line in lines:
        line = line.rstrip("\n")
        transformed += line + "#\n"
    print(transformed)
    print("---")
    return transformed


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery ===")
    filename: str = sys.argv[1]
    print(f"Accessing file {filename}")
    try:
        f1: typing.IO = open(filename, "r")
        print_content(f1)
        f1.close()
        print(f"File '{filename}' closed.")

    except Exception as e:
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")
        return
    try:
        f2: typing.IO = open(filename, "r")
        transform_data(f2)
        f2.close()
    except Exception as e:
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")
        return

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_filename: str = sys.stdin.readline().strip()
    if new_filename == "":
        print("Data not saved.")

    else:
        print(f"Saving data to '{new_filename}'")
    try:
        out: typing.IO = open(new_filename, "w")
        out.write(transform_data)
        out.close()
    except Exception as e:
        sys.stderr.write(f"STDERR] Error opening file '{new_filename}':{e}\n")
        print("Data not saved.")


if __name__ == "__main__":
    main()
