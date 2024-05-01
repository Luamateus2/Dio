from menu import depositar,extrato


saldo = float(input("Digite seu saldo inicial: "))
def menu():
    global saldo
    while True:
        opcao = int(input("0 - SAI\n1 - DEPOSITAR\n2 - EXTRATO\n3 - SAQUE\n"))
        match opcao:
            case 0: 
                return False
            case 1: 
                depositar()
            case 2: 
                extrato()
            case _: 
                print('Comando Inválido')


menu()              
