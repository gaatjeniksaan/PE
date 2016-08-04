from math import sqrt
import time

s = time.time()
num = 1
pcnt = 0
list = []

def prime(n):
    sqroot = int(sqrt(n))
    j = 2
    while j <= sqroot:
        if n % j == 0:
            return False
        j = j + 1
    return True


while (1):
    num = num + 1
    if prime(num):
        list.append(num)
    if pcnt == 2000000:
        print(pcnt, 'th prime is', num)
        break

print
time.time() - s