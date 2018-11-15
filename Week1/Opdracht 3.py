def make_prime(size):
    prime_list = []
    mark = size+1

    for i in range(2,size):
        prime_list.append(i)

    for i in prime_list:
        for j in prime_list[i:]:
            if j%i == 0:
                prime_list[prime_list.index(j)] = mark

    while mark in prime_list:
        prime_list.remove(mark)

    print(prime_list)

make_prime(1000)