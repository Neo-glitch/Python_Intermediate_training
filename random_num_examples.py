"""
this method not advicable for security reasons
since can be randomness can be reporoduced with seed
not used for auto generated keys or otp and all that
"""
import random

random.seed(1)   # to get consistency in randomness

a = random.random()  # float btw 0 and 1
a = random.uniform(1, 10)   # float btw 1 and 10
a = random.randrange(1, 10)   # int from 1 -10 excluding 10
a = random.randint(1, 10)  # int from 1-10 including 10

# random normal from standard distro with mean of 0 and std of 1
a = random.normalvariate(0, 1)

print(a)


mylist = list("ABCDEFGH")
a = random.choice(mylist)  # picks one elem
a = random.sample(mylist, 2)  # picks 2 unique elem
a = random.choices(mylist, k=2)   # picks 2 element that can be repeated
print(a)
random.shuffle(mylist)
print(mylist)



#### Secrets portion, more secure than random
import secrets

print("\nsecrets section")
a = secrets.randbelow(10) # 0-10 excluding 10
a = secrets.randbits(k = 4)  # int with k random bits and conv to dec
print(a)

myList = list("ABCDEFGH")
a = secrets.choice(myList)   # gets random unique elem
print(a)

###############

##### numpy ######
import numpy as np


a = np.random.rand(3)   #array with random floats with 3 elements(1, 3)
a = np.random.randint(0, 10, (3,2)) #int array from 0-10 of size(3,2)
print(f"\n{a}")

arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(arr)
np.random.shuffle(arr)
print(f"\n{arr}")