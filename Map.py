thelist = range(1, 11)

def double_num(num):
    return num * 2

# output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(list(map(double_num, thelist)))

# output: [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
print(list(map((lambda x: x *3 ), thelist)))

theList2 = list(map((lambda x, y: x + y), [1, 2, 3], [4, 5, 6]))
print(theList2)

# Filter
# print the even value from the list

theList3 = list(filter((lambda x : x %2 ==0), range(1, 21)))
print(theList3)