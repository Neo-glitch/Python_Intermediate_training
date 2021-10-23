def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key, value in enumerate(kwargs):
        print(key, value)

def foo_forced_keyword1(*args, c, d):
    print(c, d)

def foo_force_keyword2(a, b, *, c, d):
    print(c, d)


foo_forced_keyword1(1, 2, 
3, 4, 5,   # args
c=6, d =7 # kwargs
)

foo_forced_keyword1(1, 2, 
c=6, d =7 # kwargs
)


##unpacking list or tuple into func(len of list == no of params)
def foo_fun(a, b, c):
    print("unpacking list or dict")
    print(a, b, c)

my_list = [0, 1, 2]
foo_fun(*my_list)


# unpacking dict, keys == name of param, len of dict == no of params
my_dict = {"a":1, "b": 2, "c": 3}
foo_fun(**my_dict)



#### local and global var
number = 0

def foo_var():
    global number

    x = number
    number = 3
    print("number inside function: ", x)

foo_var()
print(number)

### Parameter passing
def foo_param(x_int_or_list):
    if(type(x_int_or_list).__name__ == "list"):
        x_int_or_list.append(4)
        return
    x_int_or_list = 5

# immutable obj can't be modfied in a func
var = 10
foo_param(var)


# mutable obj being modified in a func
my_list = [1, 2, 3]
foo_param(my_list)
print(my_list)