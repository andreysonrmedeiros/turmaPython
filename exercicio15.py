def miss():
    maior = 0
    mVencedora = ''

    for i in range (1, 17):
        candidata = input(f'Digite o nome da {i}° candidata ')
        nota = -1

        while (nota < 0) or (nota > 10):
            nota = float(input(f'Digita a nota de {candidata} de 0 a 10 : '))
            if (nota < 0) or (nota > 10 ) :
                print('ERROO!! DIGITE A NOTA DE 0 A 10 !!\n')

            if (nota > maior):
                maior = nota
                mVencedora = candidata

    return f'A vencedora foi a {mVencedora} com a nota de {maior}'


