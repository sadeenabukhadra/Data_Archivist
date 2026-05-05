# Data Archivist - Cyber Archives Project

## Overview
This project simulates a secure digital archive system where data is recovered, transformed, and safely stored using Python.

It is divided into multiple exercises that progressively introduce file handling, stream management, and safe resource usage.

---

# Exercise 0: Ancient Text Recovery (ft_ancient_text)

## Goal
Read and display the contents of a file safely, similar to the `cat` command, while handling errors properly.

## Concepts
- Command-line arguments (`sys.argv`)
- File reading using `open()`
- File streams (`typing.IO`)
- Error handling (FileNotFoundError, PermissionError)

## Behavior
- Takes a filename from the command line
- Prints a header before processing
- Reads and displays file content
- Handles errors (file missing, permission denied)
- Closes file properly

## Key Idea
Safe file reading with proper error handling and controlled output.

---

# Exercise 1: Archive Creation (ft_archive_creation)

## Goal
Modify file content by adding a special archive character (`#`) at the end of each line, then optionally save the result.

## Concepts
- File reading and writing
- String manipulation
- User input (`input()`)
- File overwrite / creation

## Behavior
- Reads file content
- Adds `#` at the end of each line
- Displays modified content
- Asks user for output filename
- Saves file if a name is provided

## Key Idea
Transform file data and persist changes safely.

---

# Exercise 2: Stream Management (ft_stream_management)

## Goal
Work directly with system streams and replace `input()` with manual stdin handling.

## Concepts
- `sys.stdin`, `sys.stdout`, `sys.stderr`
- Manual input handling
- Error output streams
- Output flushing (`flush()`)

## Behavior
- Reads input from standard input stream
- Prints normal output to stdout
- Prints errors to stderr with clear prefix
- Uses `flush()` for immediate output display

## Flush Explanation
`flush()` forces Python to immediately send buffered output to the terminal.

Without it, output may be delayed due to buffering. With it, output appears instantly.

## Key Idea
Understand low-level input/output stream control.

---

# Exercise 3: Vault Security (ft_vault_security)

## Goal
Implement a secure file handler using context managers (`with`) to ensure safe file operations.

## Concepts
- Context managers (`with open()`)
- Safe resource handling
- Function design
- Return tuples (success, message)
- File reading and writing

## Function Specification
```python
secure_archive(file_name, mode=None, content=None) -> (bool, str)
