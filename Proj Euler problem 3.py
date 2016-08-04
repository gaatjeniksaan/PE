# noinspection PyUnresolvedReferences
import mpmath as m


a = 600851475142
b = m.sqrt(a)
c = 100000
l = []
l2 = []
index = 0
index2 = 0

for num in range(2,c):
    if all(num%i!=0 for i in range(2,num)):
       l.append(num)

#print(l)

while index < b:
    if a % l[index] == 0:
        a = (a / l[index])
        index2 = l[index]
        l2.append(index2)
        index = 0
        if a == 1:
            print('We did it!')
            break
        else:
            continue
    else:
        index += 1

#print(l2)
print('The fucking prime factor you are looking for is: ',max(l2))