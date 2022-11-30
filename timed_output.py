from datetime import datetime
import sys
from my_write import my_write

original_write = sys.stdout.write


def timed_output(function):
    def wrapper(*args, **kwargs):
        sys.stdout.write = my_write
        result = function(*args, **kwargs)
        sys.stdout.write = original_write
        return result

    return wrapper


@timed_output
def print_greeting(name):
    print(f'Hello, {name}!')


if __name__ == "__main__":
    print_greeting("Nikita")
