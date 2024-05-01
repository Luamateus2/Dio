depositados = []
retiradas = []
dia = 0
saldo = float(input('Digite seu saldo inicial: '))

def depositar():
    global saldo
    valor = float(input('Qual o valor que deseja depositar? '))
    if valor <= 0:
        print('Não é possível depositar valor negativo')
    else:
        saldo += valor
        depositados.append(valor)
        print('Depositado com sucesso!')

def extrato():
    global saldo
    print(f'Seu extrato:')
    print(f'Saques realizados: {retiradas}')
    print(f'Depósitos realizados: {depositados}')
    print(f'Saldo: R${saldo}')

def saque():
    global dia,saldo
    if dia < 3:  
        saque = float(input('Digite o valor a ser sacado: '))
        if saque <= 500:
            if saque > saldo or saque < 0:
                print('Saldo Insuficiente ou Valor inválido!')
            else:
                saldo -= saque
                retiradas.append(saque)
                dia += 1
                print('Saque realizado com sucesso')
        else:
            print('Não pode retirar valores maiores que R$500')

