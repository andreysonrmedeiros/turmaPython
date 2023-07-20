#9. Faça o mesmo que antes, porém, ao
#invés de ler 10 números, o programa
#deverá ler e somar números até que o
#valor digitado seja zero ( 0 )

def somarAte0():
    c = 0
    n1 = 1
    soma = 0
    while n1 != 0:
        c += 1
        n1 = int(input('Digite o {} número '.format(c)))
        soma += n1
    return soma







