l = [18,19,20]

print("Original list", l)

# a
l[1] = 17
print("a",l)

# b
l.append(4)
l.append(5)
l.append(6)
print("b",l)

# c
l.pop(0)
print("c",l)

# d
l.sort()
print("d",l)
# e
l = l*2
print("e",l)

# f
l.pop(3)
l.insert(3,25)
print("f",l)