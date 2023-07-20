def imparParVetor():
    print('Digite 10 números: ')
    impar = []
    par = []
    for i in range(10):
        num = int(input(f'Digite o {i+1}° número: '))
        if num % 2 == 0:
            par.append(num)
            impar.append(0)
        else:
            impar.append(num)
            par.append(0)
    print(f'Par = {par}')
    print(f'Impar = {impar}')
