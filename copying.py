### Shallow vs Deep Copying
org = 5

copy = org  # new var with same ref(but since immutable change to copy doesn't affect org)
copy += 3

print(copy)
print(org)

# to copy immutable obj, to copy use copy module

import copy
org = [0, 1, 2, 3, 4, 5]
org_nested = [[0, 1, 2, 3, 4], [5,6, 7,8,9]]

cpy = copy.copy(org) # shallow copy
cpy_nested = copy.deepcopy(org_nested)  # deep copy(best option especially with class obj copy)

# cpy = org.copy()    #shallow copy(works well if org is one level deep not nested list)
# cpy = list(org)     #shallow copy(doesn't work well with nested list)
# cpy = org[:]        #shallow copy

cpy[0] = -10
cpy_nested[1][0] = -12
print(cpy)
print(org, "\n")

print(cpy_nested)
print(org_nested, "\n")
