def mult():
    a = ''
    for i in range(1, 10):
        for j in range(1, 10):
            a += (f'{i} * {j} = {i * j}\n')
    return a


print(mult())