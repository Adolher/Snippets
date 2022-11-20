from contextlib import contextmanager
import os

@contextmanager
def poem_files(file, mode):
    print("Opening File")
    open_poem_file = open(os.path.join(os.path.dirname(__file__), file), mode)
    try:
        yield open_poem_file
    except AttributeError as e:
        print(e)
    except Exception as e:
        print("Error: " + str(e))
    finally:
        print("Closing File")
        open_poem_file.close()

try:
    with poem_files('1poem.txt', 'r') as opened_file:
        print('Inside yield')
        opened_file.write('Rose is beautiful, Just like you.')
except FileNotFoundError as e:
    print(e)

