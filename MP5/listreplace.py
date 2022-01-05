#replace all values that are greater than 10 with 666

data = [30,7,30,2,88,44,60,40,1,53,100,72,86,
       64,40,85,3,19,63,84,17,31,95,84,99,60,
       85,74,65,38,43,80,39,70,8,21,32,68,64,
       55,88,84,49,68,70,98,21,51,3,97]

greater = 0
lessthan = 0
for i in range(50):
    if data[i] > 10:
        data.pop(i)
        data.insert(i, 666)
        greater += 1
    else:
        lessthan += 1

print("OUTPUT is",data)
print("Total equal values", greater)
print("Total not equal values", lessthan)