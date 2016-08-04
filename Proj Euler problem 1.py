# find multiples 3 or 5 below 10
a = 1000
l = []

for i in range(a):
    #print(i)
    if i%5 == 0:
        l.append(i)
    elif i%3 == 0:
        l.append(i)
    else:
        continue

print(sum(l))