#find 100!

def find_factorial(factorial):
    i = factorial
    p = 1
    while i > 1:
        p = p*i
        i -= 1
    return p


summ = 0
string = str(find_factorial(100))

for i in string:
     summ += int(i)

print(summ)
#find_factorial(100)