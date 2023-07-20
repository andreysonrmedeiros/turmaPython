#4 Faça um algoritmo que calcule a soma
# dos números inteiros de 1 a 100

def somar():
    soma = 0
    for i in range(1, 101, 1):
      soma += i
    return 'A soma dos elementos de 1 a 100 é {} '.format(soma)

