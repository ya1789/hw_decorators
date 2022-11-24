from datetime import datetime
import sys

original_write = sys.stdout.write


def my_write(string_text):
    now = str('[' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '] ')
    if (string_text != '\n') & (string_text is not None):
        original_write(now)
        original_write(string_text)
        original_write('\n')

    pass  # Write your own code


sys.stdout.write = my_write
print('1, 2, 3  ')


def timed_output(function):
    def wrapper(some_input):
        my_write(function(some_input))
        pass

    return wrapper


@timed_output
def print_greeting(name):
    print(f'Hello, {name}!')


print_greeting("Nikita")


def redirect_output(filepath):
    def dec_for_func(function):
        def wrapper(*args):
            with open(filepath, 'w') as f:
                original_stdout = sys.stdout
                sys.stdout = f
                function(*args)
            sys.stdout = original_stdout

        return wrapper

    return dec_for_func


@redirect_output('/home/kseniya/Desktop/function_output.txt')
def calculate():
    for power in range(1, 5):
        for num in range(1, 20):
            print(num ** power, end=' ')
        print()


calculate()
