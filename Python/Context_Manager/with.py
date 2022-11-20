import os

name = "file_name.txt"
new_name = "new_file.txt"
file_name = os.path.join(os.path.dirname(__file__), name)
new_file_name = os.path.join(os.path.dirname(__file__), new_name)

with open(file_name, "w") as open_file:
    open_file.write("How you gonna win when you ain't right within?\n")

# without context manager
try:
    open_file = open(file_name, 'r')
    print(open_file.read())
finally:
    open_file.close()

# with context manager 'with'
with open(file_name, 'r') as open_file:
    print(open_file.read())

# nested context managers ( one line )
with open(file_name, "r") as read_file, open(new_file_name, "a") as write_file:
    write_file.write(read_file.read())

# nested context managers
with open(file_name, "r") as read_file:
    with open(new_file_name, "a") as write_file:
        write_file.write(read_file.read())
