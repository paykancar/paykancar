def zarayeb(input_number):
    n = input_number
    file = open(f'multiples{n}.txt', 'w')
    file.write(f'multiple numbers of {n}\n')
    while n < 1000:
        file.write(f'{n}\n')
        n += input_number
    file.close()