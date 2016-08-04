
#
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
# 999 * 999 = 998001

list = []
for i in range(100,1000):
    for j in range(100,1000):
        k = (i*j)
        l = str(k)
        m = l[::-1]
        if l == m:
            list.append(k)




print(list)