from exercicio04 import somar
from exercicio05 import taboada
from exercicio05 import coletarPositivo
from exercicio06 import inicialFinal
from exercicio07 import impar100a200
from exercicio08 import soma10
from exercicio09 import somarAte0
from exercicio10 import mediaAte0
from exercicio11 import maiorMenor
from exercicio12 import ex12
from exercicio13 import fatorial
from exercicio14 import volei
from exercicio15 import miss
from exercicio16 import eleicao
from exercicio17 import custototal
from exercicio18 import idade
from exercicio19 import maiorNumVetor
from exercicio20 import imparParVetor
from VETORES import consultarVetor
from VETORES import preencherVetor
from VETORES import apagarPosicao
def mostrarMenu():
    print('\n\n\nEscolha uma das opções abaixo: ' +
          '\n0.  SAIR' +
          '\n1.  Exercício 01' +
          '\n2.  Exercício 02' +
          '\n3.  Exercício 03' +
          '\n4.  Exercício 04' +
          '\n5.  Exercício 05' +
          '\n6.  Exercício 06' +
          '\n7.  Exercício 07' +
          '\n8.  Exercício 08' +
          '\n9.  Exercício 09' +
          '\n10. Exercício 10' +
          '\n11. Exercício 11' +
          '\n12. Exercício 12' +
          '\n13. Exercício 13' +
          '\n14. Exercício 14' +
          '\n15. Exercício 15' +
          '\n16. Exercício 16' +
          '\n17. Exercício 17' +
          '\n18. Exercício 18' +
          '\n19. Exercício 19' +
          '\n20. Exercício 20' +
          '\n21. Preencher Vetor' +
          '\n22. Consultar Vetor' +
          '\n23. Apagar posição vetor.')

def operacao():
    #chamar outro método
    while True:
        mostrarMenu()
        #coletar opção do úsuario
        opcao = int(input('Digite aqui o número da opção escolhida: '))
        #executar a ação
        if (opcao == 0):
            #instruções do exercicio01
            print('Obrigado')
            break
        elif(opcao == 1 ):
            return
        elif (opcao ==2 ):
            return
        elif (opcao ==3 ):
            return
        elif (opcao == 4):

        #Exercicio04
            print('\n Exercicio04')
            print(somar())

        elif (opcao == 5):

        # Exercicio05
            print('\n Exercicio05')
            num = int(input('Digite um número para descobrir a taboada: '))
            print('Até que número será multiplicado? ')
            n = coletarPositivo()
            taboada(num, n)

        elif (opcao == 6):

        # Exercicio06
            print('\n Exercicio06')
            n1 = int(input('Digite um número '))
            n2 = int(input('Digite outro número '))
            inicialFinal(n1, n2)

        elif (opcao == 7):

        # exercicio07
            print('\n Exercicio07')
            impar100a200()

        elif (opcao == 8):

        # Exercicio08
            print('\nExercicio08')
            print('Digite 10 números e descubra a sua somatória')
            print('A soma dos números digitados é igual a {}'.format(soma10()))

        elif (opcao == 9):

        # Exercicio09
            print('\nExercicio09')
            print('Digite números para descobrir o valor da somatória, digite 0 para encerrar')
            print(somarAte0())

        elif (opcao == 10):

        # Exercicio10
            print('\nExercicio10')
            print('Digite números e descubra a somatória dos números pares, digite 0 para encerrar!!')
            print(mediaAte0())

        elif (opcao == 11):

        # Exercicio11
            print('\nExercicio11')
            print(maiorMenor())

        elif (opcao == 12):

        # Exercicio12
            print('\nExercicio12')
            print(ex12())

        elif (opcao == 13):
            # Exercicio13
            print('\nExercicio13')
            n1 = int(input('Digite um número e descubra o seu fatorial '))
            print('O fatorial de {} é {}'.format(n1, fatorial(n1)))

        elif (opcao == 14):
            # exercicio 14
            print(volei())
        elif (opcao == 15):
            # Exercicio 15
            print(miss())
        elif (opcao == 16):
            #Exercicio 16
            print(eleicao())
        elif (opcao == 17):
            #Exercicio 17
            custototal()
        elif (opcao == 18):
            #Exercicio18
            idade()
        elif (opcao == 19):
            #exercicio19
            print('Digite 5 números inteiro')
            print(maiorNumVetor())
        elif (opcao == 20):
            #exercicio20
            imparParVetor()
        elif (opcao == 21):
            num = int(input('Informe o tamanho do vetor: '))
            preencherVetor(num)
        elif (opcao == 22 ):
            num = int(input('Informe até que posição do vetor: '))
            consultarVetor(num)
        elif (opcao == 23):
            posicao = int(input('Infome a posição que deseja apagar.'))
            apagarPosicao(posicao-1)

        else:
            print('Opção escolhida não é válida, digite novamente!')







