from datetime import datetime
import sys

original_write = sys.stdout.write


def my_write(string_text):
    if (string_text != '\n') & (string_text is not None):
        f_string = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {string_text}\n"
        original_write(f_string)
    else:
        original_write(string_text)


if __name__ == "__main__":
    print('1, 2, 3  ')
    print('\n')
