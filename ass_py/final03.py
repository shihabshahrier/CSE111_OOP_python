from math import pi

n = int(input("Enter N: "))
dict1 = {}
list1 = []
for i in range(n):
    r = int(input(f"Enter Radious {i+1}: "))
    list1.append(r)

for i in range(len(list1)):
    dict1[f"Circle {i}"]=[pi*(list1[i]**2), 2*pi*list1[i]]

print(dict1)
    