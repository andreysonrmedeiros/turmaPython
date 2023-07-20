def eleicao():

    while True:
        etotal = int(input('Digite o número total de eleitores: '))
        if etotal <= 0:
            print('O número total de eleitores tem que ser positivo! tente novamente')
        else:
            break

    while True:
        brancos = int(input('Digite o total de votos brancos: '))
        if brancos < 0:
            print('O número de votos brancos não pode ser negativo')
        elif brancos > etotal:
            print('O número de votos brancos ultrapassou o total de eleitores, tente novamente!')
        else:
            break

    while True:
        nulos = int(input('Digite o total de votos nulos: '))
        if nulos < 0:
            print('O número de votos nulos não pode ser negativo')
        elif nulos > etotal or ( nulos + brancos) > etotal:
            print('O número de votos nulos ultrapassou o total de eleitores, tente novamente!')
        else:
            break

    while True:
        validos = int(input('Digite o total de votos válidos: '))
        if validos < 0:
            print('O número de votos nulos não pode ser negativo')
        elif validos > etotal or (validos+nulos+brancos) > etotal:
            print('O número de votos válidos ultrapassou o total de eleitores, tente novamente!')
        else:
            break



    brancoP = (brancos * 100)/ etotal
    nulosP = (nulos * 100)/ etotal
    validosP = (validos * 100) / etotal

    return f'Os votos brancos equivalem a {(brancoP):.2f}% do total de eleitores\n' \
           f'Os votos nulos {(nulosP):.2f}%\n' \
           f'os votos validos {(validosP):.2f}% do total de eleitores do município'


