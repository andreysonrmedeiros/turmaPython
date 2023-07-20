def custototal():
    print('Calcule o custo total do veículo \n')
    custo = float(input('Digite o custo de fabrica do véiculo: '))
    distribuidor = (28*custo)/100
    imposto =(45*custo)/100
    custoT = custo + distribuidor + imposto
    print(f'O custo total do veículo é R$ {(custoT):.2f} reais')

