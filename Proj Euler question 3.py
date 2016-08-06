a = 600851475143
n = 10002
l = [] #list with prime numbers between 2 and 1000
l2 = [a] #list to append with prime factors


for p in range(2, n+1):
    for i in range(2, p):
        if p % i == 0:
            break
    else:
        l.append(p)
print("Done")

il = 0 #index for looping through l (list with prime numbers)
il2 = 0

#begin met l2[0] % l[0] == int (lukt dat? JA => dan het modular resultaat opslaan in l2.
#vervolgens l2[1] % l[0] == int? nee? dan l2[1] % l[1], etc.
#vervolgens maximum van l2 en voila
#zodra l2[i] % whatever == 0: break
#ik moet dus twee indici hebben voor loopen, eentje die gereset wordt voor l en eentje die blijft bestaan voor l2



while True:


    if ((l2[il2] % l[il])).is_integer() == True:
        print('het lukt')
        break
    else:
        print('het lukt niet')
        il += 1

#
# for i in range(len(l)):
#     if (l2[i-1] % l(index)) == int:
#         l2.append(l2[i-1]%l(index))
#         index = 0
#     else:
#         index += 1


print(l2)


