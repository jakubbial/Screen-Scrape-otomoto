# Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

Less_than_two_1 = []

for a in list:
    if a < 5:
        Less_than_two_1.append(a)
print(Less_than_two_1)

# One line
print([element for element in list if element <5])

# Less_than_two_2=[]
# Less_than_two_2.append(thing) if thing < 5 else False for thing in list
# print(Less_than_two_2)
