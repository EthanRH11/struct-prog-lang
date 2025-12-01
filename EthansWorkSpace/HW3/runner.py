#!/usr/bin/env python

import sys
from tokenizer import tokenize
from parser import parse
from evaluator import evaluate, set_watched_variable

def main():
    environment = {}

    # Parse command line arguments
    watch_var = None
    file_to_run = None

    for arg in sys.argv[1:]:
        if arg.startswith("watch="):
            watch_var = arg.split("=", 1)[1]
        else:
            file_to_run = arg  # Assume the first non-watch argument is the file

    # Set watched variable if provided
    if watch_var:
        set_watched_variable(watch_var)

    if file_to_run:
        # Filename provided, read and execute it
        try:
            with open(file_to_run, 'r') as f:
                source_code = f.read()
            tokens = tokenize(source_code)
            ast = parse(tokens)
            final_value, exit_status = evaluate(ast, environment)
            if exit_status == "exit":
                sys.exit(final_value if isinstance(final_value, int) else 0)
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)  # Indicate error to OS
    else:
        # REPL loop
        while True:
            try:
                source_code = input('>> ')

                if source_code.strip() in ['exit', 'quit']:
                    break

                tokens = tokenize(source_code)
                ast = parse(tokens)
                final_value, exit_status = evaluate(ast, environment)
                if exit_status == "exit":
                    print(f"Exiting with code: {final_value}")
                    sys.exit(final_value if isinstance(final_value, int) else 0)
                elif final_value is not None:
                    print(final_value)
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    main()
