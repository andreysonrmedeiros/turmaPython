def ex12():
    i = 0
    n = 0
    soma = 0
    impar = 0
    print('Digite 20 números:')

    for i in range(1,21):
        n = int(input('Digite o {}° número: '.format(i)))
        if n >= 0:
            soma += n
        if n < 0:
            impar += 1


    return 'A soma dos números positivos é igual a {} , você digitou {} números negativos'.format(soma, impar)


