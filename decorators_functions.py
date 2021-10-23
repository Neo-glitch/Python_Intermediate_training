import functools

def start_end_decorator(func):

    # inner function called wrapper, decorator here
    # is to preserve info of used function
    # not needed though
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("start of inner func")
        result = func(*args, **kwargs)
        print("end of inner func")
        return result
    return wrapper


@start_end_decorator # if decorator not used used syntax below
def print_name():
    print("Alex")


@start_end_decorator
def add5(x):
    print("adding")
    return x + 5


# function taking func, what is ret is the inner func
# print_name = start_end_decorator(print_name)

print_name()

result = add5(20)
print(result)


print("\n")
print(help(add5))
print(add5.__name__)



#### another decorator example, decorator that takes also
#### arg that aren't func 

def repeat(num_times):

    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            for i in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat



@repeat(num_times = 3)
def greet(name):
    print("Hello {}".format(name))


greet("nnena")




#### another example, nested decorators(stacking dec onoTop of each other)
def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k} = {v!r}" for k, v in kwargs.items()]

        # gets the name and arg and kwargs and print the info of this func
        # exec the func and prints info about return value
        signature=",".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper



@debug               #runs first 
@start_end_decorator #then exec this func(now inner func) and then say_hello
def say_hello(name):
    greeting = f"Hello {name}"
    print(greeting)
    return greeting



say_hello("benjamin")