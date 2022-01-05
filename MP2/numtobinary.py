num = int(input("Enter a number: "))

binary = format(num, "b")

for i in reversed(binary):
    print(i)