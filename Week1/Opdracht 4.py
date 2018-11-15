import random

counter = 0

for i in range(0, 100):
    list = []
    for j in range(0, 23):
        list.append(random.randrange(1,366))
    for k in list:
        if k in list[list.index(k)+1:]:
            counter += 1
            break
counter /= 100
print(counter, '%', sep='')