def idade():
    print('Digite sua idade completa com Ano(s), Mes(es) e dia(s): ')
    ano = int(input('Ano(s): '))
    mes = int(input('Mês(es): '))
    dia = int(input('Dia(s): '))

    anoD = ano * 365
    mesD = mes * 30
    diaT = anoD + mesD + dia
    print(f'Você ja viveu {diaT} dias')

