import os

# The use of __enter__() and __exit__()
class ContextManager:
    def __init__(self):
        print('Initializing class...')
 
    def __enter__(self):
        print('Entering context...')
 
    def __exit__(self, *exc):
        print('Exiting context...')

with ContextManager() as cm:
    print("Code inside with statement")

print() # open and close a file
class WorkWithFile:
    def __init__(self, file, path=None, mode="r"):
        self.file = file
        if path is not None:
            self.file_path = path
        else:
            self.file_path  = os.path.join(os.path.dirname(__file__), self.file)
        self.mode = mode

    def __enter__(self):
        self.opened_file = open(self.file_path, self.mode)
        return self.opened_file

    def __exit__(self, *exc):
        self.opened_file.close()

with WorkWithFile("file_name.txt") as file:
    print(file.read())
    print()

# ErrorHandling in the __exit__() method
class ErrorHandling:
    def __init__(self, file, path=None, mode="r"):
        self.file = file
        if path is not None:
            self.file_path = path
        else:
            self.file_path  = os.path.join(os.path.dirname(__file__), self.file)
        self.mode = mode

    def __enter__(self):
        self.opened_file = open(self.file_path, self.mode)
        return self.opened_file

    def __exit__(self, exc_type, exc_value, traceback): # , *exc):    *exc stands for exception and contains the arguments type, value and traceback
        if isinstance(exc_value, AttributeError):
            print(f"Exception Type is:\t {exc_type}")
            print(f"Exception Value is:\t {exc_value}")
            print(f"Traceback is:\t\t {traceback}")
            print("The Exception has been handeled")
            self.opened_file.close()
            return True     # suppress (unterdrücken) the Exception with 'True'
        self.opened_file.close()
        
        

with ErrorHandling("file_name.txt") as file:
    print(file.read())
    print()
    print(file.see())