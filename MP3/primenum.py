def nextPrimeList(n):
    primenum = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for i in range(len(primenum)):
        if (n < primenum[i]):
            return primenum[i]
            break


n = input("Enter a positive number: ")
t1 = float(n)
n = float(n)
n = int(n)


while(n != t1):
    print("The number should be whole value.")
    n = input("Enter a positive integer: ")
    t2 = float(n)
    if (int(t2) == int(n)):
        break

while n<0:
    print("The number is not a positive integer")
    n = input("Enter a positive integer: ")
    if n>=0:
        break;

print("The first prime greater than the number entered is: ", nextPrimeList(n))