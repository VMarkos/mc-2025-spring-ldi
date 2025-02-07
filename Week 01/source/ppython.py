# ppython.py

import sys

from Token import Token
import Scanner

# Error handling
# You should properly utilise the functions below to print errors
# when you should in `run()` or elsewhere.
# You will have to modify those functions in future labs (or even
# this lab) to utilise them in more places.

def error(line: int, message: str) -> None:
    report(line, message)

def report(line: int, message: str) -> None:
    print(f"{line} | Error: {message}")

# Running ppython

def run(source: str) -> None:
    scanner: Scanner = Scanner.Scanner(source)
    tokens: list[Token] = scanner.scan_tokens()

    # Just a dummy way to implement `run()` for Lab 01.    
    for token in tokens:
        print(token)

def run_prompt() -> None:
    while True:
        print(">>> ", end = "")
        line = input()
        if line == "exit()":
            break
        run(line)

def run_file(path: str) -> None:
    pass
    # this is to be implemented by you.
    # Youd should properly parse the file and then wrap `run()` to
    # actually execute every command into the script.
    # Evidently, you should modify `run()` to properly execute commands
    # in the future. For now, just print tokens.

def main() -> None:
    args = sys.argv
    if len(args) == 2:
        run_file(args[1])
    elif len(args) == 1:
        run_prompt()
    else:
        print("Usage: python[3] ppython.py [script.py]")
        exit(64)

if __name__ == "__main__":
    main()