#7 Escrever um algoritmo que gera e
#escreve os números ímpares entre 100 e 200

def impar100a200():
        msg = ''
        print('Os números impar de 100 a 200 são: ')
        for i in range(100, 201):
            if (i % 2 == 1):
                msg += str(i) + ' '
        print(msg)