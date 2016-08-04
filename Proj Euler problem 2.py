n = 1
l = []
a = 0
b = 0

x = [1,1]
sum_list = []
for i in range(100):
    x.append((x[-1] + x[-2]))
print(', '.join(str(y) for y in x))

for i in x:
    if i <= 4000000:
        if i%2 == 0:
            print(i)
            sum_list.append(i)
        else:
            continue
    else:
        break

c = sum(sum_list)
print('the final sum is:', c)







