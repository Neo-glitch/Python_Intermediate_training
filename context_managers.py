from threading import Lock
from contextlib import contextmanager

# context manager(closes file when needed, even if error found)
with open("notes.txt", "w") as file:
    file.write("some todos....")

# another example

lock = Lock()

# with lock:
#     ###...

# implementing Context Manager for our class


class ManagedFile:
    def __init__(self, filename):
        self.filename = filename

    """
    exec as soon as 'with' statement
    is entered
    """

    def __enter__(self):
        print("enter")
        self.file = open(self.filename, "w")
        return self.file      # ret back the allocated resource

    def __exit__(self, exc_type, exc_value, exc_tb):
        # to correctly close file no matter what, exeption found or not
        # and handle exception adequately
        if self.file:
            self.file.close()
        if(exc_type is not None):
            print("exception has been handled")
        # print("exe:", exc_type, exc_value)
        print("exit")
        return True   # done inorder to not raise exception in main program


with ManagedFile("notes.tXt") as file:
    print("doing some stuff")
    file.write("some todooooo")
    file.somemethod()

print("continuing")


@contextmanager
def open_managed_file(filename):
    f = open(filename, "w")
    try:
        yield f
    finally:
        f.close()


with open_managed_file("notes.txt") as file:
    file.write("This is the function written to the text")
