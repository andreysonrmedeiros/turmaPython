#6 Faça um algoritmo que escreva na tela
#os números de um número inicial a um
#número final. Os números inicial e final
#devem ser informados pelo usuário

def inicialFinal(n1, n2):

    print('A sequencia de {} a {} é: '.format(n1, n2))

    msg = ''
    if (n1 < n2):
        for i in range(n1, n2 + 1):
            msg += str(i) + ' '

        print(msg)

    else:
        for i in range(n1, n2-1, -1):
            msg += str(i) + ' '

        print(msg)
