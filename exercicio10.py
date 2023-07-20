def mediaAte0():
    c = 1
    n1 = 1
    media = 0
    soma = 0
    while n1 != 0:
        n1 = (int(input('Digite o {} número '.format(c))))
        if n1 != 0:
            if n1 % 2 == 0:
                soma += n1
                media = soma / c
                c += 1
    return 'A média dos números pares digitados é igual a {}'.format(media)
