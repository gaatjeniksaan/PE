def triangle(number):
    """returns a list with the first triangular numbers with length equal to argument"""
    list = [1]
    sum = 1
    for i in range(2,number+1):
        sum += i
        list.append(sum)
    return list

def iprimes_upto(limit):
    """returns a list with all prime numbers up to argument if called with list(iprimes_upto(argument))"""
    is_prime = [True] * limit
    for n in range(2, limit):
        if is_prime[n]:
           yield n
           for i in range(n*n, limit, n): # start at ``n`` squared
               is_prime[i] = False

def sum_factors(input):
    """returns a list with count of prime factors"""
    list_pf = [0]*(len(list(iprimes_upto(input)))) #create empty list with length of amount of primes in input
    l = list(iprimes_upto(input)) #creates list with all primes < input
    index = 0
    # print(list_pf, l)
    while True:
        if input == 1:
            return list_pf
            break
        elif index == len(l):
            # print('party is over')
            break
        elif (input % l[index]) == 0:
            input = int(input / l[index])
            list_pf[index] += 1
            index = 0
            # print(input)
        else:
            index += 1


# sum_factors(10000)

def check_factor_count(check):
    """takes list as input to count the amount of factors corresponding to the list"""
    while 0 in check: check.remove(0) #removes all zeros from list
    for i in range(0,len(check)): check[i] += 1 #adds one to all factor counts
    product = 1
    for j in check: product *= j
    return product

check_factor_count(sum_factors(100000))

n = 1000000







