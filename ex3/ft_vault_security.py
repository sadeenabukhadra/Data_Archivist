def secure_archive(file_name: str, mode: str, content: str) -> tuple[bool, str]:
    if mode == "r":
        try:
            with open(file_name, "r") as f:
                data = f.read()
            return (True, data)
        except Exception as e:
            return (False, str(e))

    else:
        try:
            with open(file_name, "w") as f:
                f.write(content)
            return (True, "Content successfully written to file")
        except Exception as e:
            return (False, str(e))


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "r", ""))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd", "r", ""))

    print("\nUsing 'secure_archive' to read from a regular file:")
    print(secure_archive("test.txt", "r", ""))

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_file.txt", "w", "Hello Vault Security"))