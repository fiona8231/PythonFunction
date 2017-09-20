
# Function 1
def mult_by_2(num):
    return num * 2

times_two = mult_by_2(3)
print("3 * 2 = ", times_two)

# Function 2
def do_math(function, num):
    return function(num)

print("8 * 2 =", do_math(mult_by_2, 8))

# Function 3 function inside function

def get_function_multby(num):
    def mult_by(value):
        return num * value
    # Return a function from a function
    return mult_by

generated_func = get_function_multby(5)

print("5 * 10 = ", generated_func(10))

# Functions list

listOfFuns = [times_two, generated_func]

# listofFuns[1] -> put in the first element of list,
# 5 -> from generated_func = get_function_multby(5)

# has nothing to do with times_two function for calculating
print("5 * 6 = ", listOfFuns[1](6))