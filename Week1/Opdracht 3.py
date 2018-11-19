# Naam: Deniz Lektemur
# Studentnummer: 1722313
# Klas: V2C
# Docent: Frits Dannenberg

numbers_list = []
prime_list = []
mark_list = [False] * 999

for i in range(2, 1001):
    numbers_list.append(i)

for j in numbers_list:
    counter = 2
    number = j * counter
    while number < 1001:
        mark_list[numbers_list.index(number)] = True
        counter += 1
        number = j * counter

for k in range(len(mark_list)):
    if mark_list[k] == False:
        prime_list.append(numbers_list[k])

print(prime_list)
