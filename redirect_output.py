import sys


def redirect_output(filepath):
    def dec_for_func(function):
        def wrapper(*args, **kwargs):
            with open(filepath, 'w') as file:
                original_stdout = sys.stdout
                sys.stdout = file
                function(*args, **kwargs)
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
