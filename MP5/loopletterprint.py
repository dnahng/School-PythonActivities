letters = "abcdefghijklmnopqrstuvwxyz"

list = []
cnt = 1
for i in letters:
    list.append(i*cnt)
    cnt += 1

print("OUTPUT IS", list)