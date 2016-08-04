#
#
# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.
#
#


# print(len_collatz(13))

import time

start = time.time()

sequence = []

n = 999999
length = 0
list = []

def len_collatz(number):
    index = 1
    while number > 1:
        if number%2 == 0:
            number = number / 2
            index += 1
        else:
            number = 3*number+1
            index += 1
    return index

for i in range(2,n):
    if len_collatz(i) > length:
        length = len_collatz(i)
        number = i
    finish = time.time()

print(('The largest chain is of length %s corresponding to the number %s') % (length, number))
print('Time is:', finish - start)


#
# def collatz(n):
#     sequence.append(n)
#     while sequence[-1] != 1:
#         if n % 2 == 0:
#             n //= 2
#             return collatz(n)
#         else:
#             n = (n * 3) + 1
#             return collatz(n)
#     x = len(sequence)
#     sequence.clear()
#     return x
#
#
# def solve():
#     result = 0
#     length = 0
#     for i in range(999999, 777777, -2):  # 777777 is random..
#         if collatz(i) > length:
#             length = collatz(i)
#             result = i
#     finish = time.time()
#     print("Result : ", result, "Length : ", length, "Time : ", finish - start, "Sec")  # Result : 837799 Length = 525


if __name__ == '__main__':
    solve()