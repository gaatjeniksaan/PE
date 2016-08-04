#
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
l = []

c = 100000

# for num in range(2,c):
#     if all(num%i!=0 for i in range(2,num)):
#        l.append(num)

a = 2520

while True:
    if all(a%i == 0 for i in range(2,21)):
        print(a)
        break
    else:
        a +=19


