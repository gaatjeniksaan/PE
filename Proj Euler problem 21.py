#Find sum of all amicable numbers under 10000
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

def fsd(input):
    """returns the sum of all divisors of input"""
    som = 0
    for i in range(1,input-1):
        if input % i == 0:
            som += i
    return som

summa = 0
for j in range(1,10000):
    if j == fsd(fsd(j)) and j != fsd(j):
        summa += j
        print(summa, j)


