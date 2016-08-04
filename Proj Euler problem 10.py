#
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
# noinspection PyUnresolvedReferences
from math import sqrt

c = 2000000

l = [2]
sum = 0

for num in range(3,c,2):
    if all(num%i!=0 for i in range(2,num)):
       l.append(num)

# for i in l:
#     sum += int(i)

print(sum)
print()