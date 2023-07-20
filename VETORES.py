notas = [] #vetor global

def preencherVetor(fim):
    for i in range(fim):
        num = int(input(f'Digite a {i+1}° nota: '))
        notas.append(num) #adicionando notas ao vetor

def consultarVetor(fim):
    if len(notas) < fim:
        print('A posição informada é maior que a ultima posição!')
    else:
        for i in range(fim):
            print(f'Posição {i +1} ---> {notas[i]}')

def apagarPosicao(posicao):
    if len(notas) < posicao:
        print('Impossivel remover pois o tamanho é menor que a posição.')
    else:
        del(notas[posicao]) #excluindo um dado do vetor
        print('Removido com sucesso!')
