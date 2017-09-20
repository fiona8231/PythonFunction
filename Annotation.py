
# function return string
def random_func(name: str, age:int, weight: float) -> str:
    print("Name : ", name)
    print("Age: ", age)
    print("Weight: ", weight)

    return "{} is {} years old and weihgts {}".format(name, age, weight)

print(random_func("Cat", 33, 144))

# output: 66 is Cat years old and weihgts turtle
# You don't get an error if you pass bad data
print(random_func(66, "Cat", 'turtle'))
# output : {'name': <class 'str'>, 'age': <class 'int'>, 'weight': <class 'float'>, 'return': <class 'str'>}
print(random_func.__annotations__)