def xyz_diff(p1, p2):
    for i in range(len(p1)):
        if(p1[i] != p2[i]):
            return i+1
    return -1

param1 = input("Enter first string:")
param2 = input("Enter second string:")

print(xyz_diff(param1, param2))