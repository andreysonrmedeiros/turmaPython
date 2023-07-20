def volei():
    media = 0
    time = int(input('Digite a quantidade de jogadores no time: '))
    for i in range (1, time +1):
        jogadores = float(input(f'Digite a altura do {i}° Jogador: '))
        media += jogadores

    return f'A altura média do time é {(media / time):.2f}'

