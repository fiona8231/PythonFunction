# ---------- PROBLEM ----------
# Create a random list filled with the characters H and T
# for heads and tails. Output the number of Hs and Ts

# Example Output
# Heads :  46
# Tails :  54

import random
from functools import reduce

theList = []

# Populate the list with 100 Hs and Ts
# Trick : random.choice() returns a random value from the list

# choice -> randomly choose from the list
for i in range(1, 101):
    theList += random.choice(['T', 'H'])

print(theList)

# for heads and tails. Output the number of Hs and Ts

print("Num of Heads: ", theList.count("H"))
print("Num of Tails : ", theList.count('T'))

# ---------- PROBLEM ----------
# Find the multiples of 9 from a random 100 value list with
# values between 1 and 1000

# Generate a random list with randint between 1 and 1000
# Use range to generate 100 values

# Use randint

theList2 = list(random.randint(1, 1000) for i in range(100))

theList3 = list(filter((lambda x : x % 9 ==0), theList2))
print(theList3)


print(reduce((lambda x, y: x +y ), range(1, 6)))