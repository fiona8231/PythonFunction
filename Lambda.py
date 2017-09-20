
# can not assign lambda to a name
sum = lambda x, y: x + y

print("Sum :", sum(4, 5))

can_vote = lambda age: True if age >= 18 else False

print(can_vote(16))

# Create list functions

powerList = [lambda x: x ** 2,
             lambda x: x ** 3,
             lambda x: x ** 4]

for func in powerList:
    print(func(4))

# You can also store lambdas in dictionary

attack = {'quick': (lambda: print("quick Attack")),
          'power': (lambda: print("power attack")),
          'miss': (lambda : print("Miss attack"))}

# output: quick Attack
attack['quick']()

import random

# choice -> randomly choose from the list
# and convert to list -> list()
attackKey = random.choice(list(attack.keys()))

# Output: quick Attack
# power attack
attack[attackKey]()