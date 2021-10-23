def mygenerator():
    yield 1
    yield 2
    yield 3
    yield 4


g = mygenerator()
# value = next(g)
# print(value)

# value = next(g)
# print(value)

# value = next(g)
# print(value)


# calc the sum
print(sum(g))


# another generator fun
def countdown(num):
    print("starting")
    while num > 0:
        yield num
        num -= 1

cd = countdown(3)

value = next(cd)
print(value)

value = next(cd)
print(value)



# generators for saving memory

# to create a sequence from 0 - n, without gen
def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

# to create a sequence from 0 - n, with gen(saves more memory)
# since elements are lazy int
def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1


# mylist = firstn(10)
mylist = firstn_generator(10)

print(sum(mylist))



# last useCase of gen

def fibonacci(limit):
    # fibonacci sequence = 0 1 1 2 3 5 8.....
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


fib = fibonacci(20)

print("\n")
for element in fib:
    print(element)


###### Generator expression(kinda like list comprehension)
print("\n")
mygenerator = (i for i in range(10) if i % 2 == 0)

# print(next(mygenerator))
# print(next(mygenerator))
# print(next(mygenerator))


# conv generator to list
converted_list = list(mygenerator)
print(converted_list) 
