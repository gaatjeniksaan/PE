# l = ['A','B','C','D','a','b','c']
#
# for i in l:
#     print(ord(i))


file = open('names.txt', 'r')
names = file.read()
names = names.split('","')
names[0] = "MARY"
names[len(names)-1] = "ALONSO"
names = sorted(names)
print(names)
sum = 0
sum_str = 0
index = 1

for i in names:
    for j in i:
        sum_str += ord(j)-64
    sum += index*sum_str
    sum_str = 0
    index +=1

print(sum)

file.close()

