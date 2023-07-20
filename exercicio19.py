def maiorNumVetor():
    vetor = []
    maior = 0
    for i in range(5):
        num = int(input(f'Digite o {i+1}° valor. '))
        vetor.append(num)

    for i in range (5):
        if maior == 0:
            maior = vetor[i]
        elif vetor[i] > maior:
            maior = vetor[i]

    return f'O maior número digitado foi o {maior}.'

