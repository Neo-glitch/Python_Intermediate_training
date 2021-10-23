# creating list, tuples or string with repeated element
zeros = [0, 1] * 10  # list with 10 elements of 0 and 1
strings = "AB" * 10
print(zeros, "\n")
print(strings, "\n")


# unpacking elements of a container
numbers = [1,2,3,4,5,6]

*beginning, last= numbers
print(beginning)   # all elements except last one in a list(for tuple and list)
print(last, "\n")  # last element



beginning, *last = numbers
print(beginning)   # 1st element alone
print(last, "\n")  # last element up until first element in a list


beginning, *middle, last = numbers
print(beginning)  # 1st element
print(middle)     # in between first and last element in list
print(last,"\n")       # last element alone


# merging iterables into a list
my_tuple = (1, 2, 3)
my_list = [4, 5, 6]

new_list = [*my_tuple, *my_list]
print(new_list, "\n")

my_set = {7, 8, 9}
new_list1 = [*my_list, *my_set]
print(new_list1, "\n")

dict_a = {"a":1, "b": 2}
dict_b = {"c": 3, "d":4}

my_dict = {**dict_a, **dict_b}
print(my_dict, "\n")
