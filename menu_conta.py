from cliente import cadastrar_conta,cadastrar_usuario

def menu_conta():   
    print('#####################SEJA BEM VINDO AO SISTEMA DE CADASTRO DE CLIENTE E CONTA #######################################')
    while True:
        opcao = int(input('0-PARA SAIR \n 1-PARA CADASTRAR UM USUÁRIOS \n 2-PARA CRIAR UMA CONTA'))
        match opcao:
            case 0: return False
            case 1: cadastrar_usuario()
            case 2: cadastrar_conta()
            case _: print('Comando Inválido')
        
