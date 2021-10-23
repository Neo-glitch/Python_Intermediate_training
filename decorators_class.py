# class decorator
class CountCalls:

    def __init__(self, func):
        self.func = func
        self.num_calls = 0  # what we are keeping track of

    # must be implemented for class dec, where we can exec the func
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"This is executed {self.num_calls} times")
        return self.func(*args, **kwargs)


@CountCalls
def say_hello():
    print("Hello")


say_hello()
say_hello()
say_hello()





"""
some use cases of decorators are:
timer decorator = to calc exec time of fun
debug decorator = to print out some more ino about a called fun(stacking stuff)
check decor = to check if arg will pass some requirements and behave accordingly
decorator to register func like plugins
To cache return values or update state as seen here
"""