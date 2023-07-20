#5 Construa um programa que exiba a
#tabuada de 1 até N.

def taboada(num, n):
    for i in range(1, n+1):
        print('{} X {} = {}'.format(num, i, num * i))

def coletarPositivo():
    num = int(input('Informe um número '))
    while(num < 0):
        print('ERRO! informe um número positivo ')
        num = int(input('Informe um número positvo para multiplicar '))
    return num
