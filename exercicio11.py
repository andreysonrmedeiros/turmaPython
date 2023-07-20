def maiorMenor():
    n = 1
    c = 1
    maior = 0
    menor = 0
    print('Digite números inteiros e descubra o maior e o menor')
    while n != 0:
        n = int(input('Digite o {}° número: '.format(c)))
        c += 1
        if menor == 0:
            menor = n
        if n > maior:
            maior = n
        if n < menor and n != 0:
            menor = n

    return 'O maior número digitado foi {} e o menor {}'. format(maior, menor)

