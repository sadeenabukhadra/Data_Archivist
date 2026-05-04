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
        transformed_line = line + "#\n"
        print(transformed_line, end="")
        transformed += transformed_line

    print("---")
    return transformed

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    print("=== Cyber Archives Recovery & Preservation ===")

    filename: str = sys.argv[1]
    print(f"Accessing file '{filename}'")

    try:
        f1: typing.IO = open(filename, "r")
        print_content(f1)
        f1.close()
        print(f"File '{filename}' closed.")

        f2: typing.IO = open(filename, "r")
        transformed: str = transform_data(f2)
        f2.close()

        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()

        new_filename: str = sys.stdin.readline().strip()

        if new_filename == "":
            print("Not saving data.")
        else:
            print(f"Saving data to '{new_filename}'")

            try:
                f_out: typing.IO = open(new_filename, "w")
                f_out.write(transformed)
                f_out.close()
                print(f"Data saved in file '{new_filename}'.")
            except Exception as e:
                sys.stderr.write(f"[STDERR] Error opening file '{new_filename}': {e}\n")
                print("Data not saved.")

    except Exception as e:
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")

if __name__ == "__main__":
    main()