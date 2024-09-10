legenda = """==============================================
             Desafio de python
==============================================
"""
print(legenda)
operacao_bancaria = ''
saldo = 0
extrato = []

while True:
    operacao = input('Qual operação você quer realizar?\nDeposito: [a]\nSaque: [b]\nExibir extrato: [c]: \nSair: [s]\n>>Digite sua opção: ')
    print(operacao)
    if operacao == 'a':
        deposito  = float(input('qual valor você quer depositar: R$'))
        if deposito >= 0:
            saldo += deposito
            extrato.append(deposito)
        else:
            print('não permitidos depositos negativos')
    elif operacao == 'b':
        saque = float(input('qual valor você quer sacar'))
        if saque >= 0:
            saldo -= saque
        else:
            print('não sao permitidos valores negativos')
    elif operacao == 'c':
        for movimentação in extrato:
            print(movimentação)


    elif operacao == 's':
        print('Tenha um bom dia')
        break
print('Fim da operação')
print(extrato)

