import math

values = [-1,-5,4,-2]

root = abs(sum(values))

tree = [root]

def split(list):
    if len(list) == 1:
        return abs(list[0])
    a = list[0:(len(list)//2)]
    b = list[(len(list)//2):]
    tree.append(abs(sum(a)))
    tree.append(abs(sum(b)))
    split(a)
    split(b)

split(values)

print(tree)