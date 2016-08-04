n = 1
l = []
a = 0
b = 0
index = 1
x = [1,1]
sum_list = []
for i in range(1000000):
    x.append((x[-1] + x[-2]))
    if len(str(x[i]))== 1000:
        print(x[i], index)
        break
    index += 1
# print(', '.join(str(y) for y in x))