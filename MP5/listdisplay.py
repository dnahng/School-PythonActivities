L = [63,52,10,42,32,17,60,45,47,39,71,55,41,95,70,48,42,32,13,35]

# a
print("Display LIST ",L)

# b
length = len(L)
avg = sum(L)/length
print("AVERAGE",avg)

# c
print("SMALLEST/LARGEST ", min(L), max(L))

# d
L.sort()
secmax = L[length - 2]
secmin = L[1]
print("2nd SMALLEST/LARGEST", secmin, secmax)

# e & f
even = 0
odd = 0
for num in L:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Total number of Even numbers ", even)
print("Total number of Odd numbers ", odd)