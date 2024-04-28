usuarios ={}
contas ={}
prox_numero_conta = 1

def cadastrar_usuario():
    nome = input('Digite seu nome: ')
    dt_nascimento = input('Digite sua data de nascimento: ')
    cpf = input('Digite seu cpf: ')
    endereco = input('Digite seu endereço: ')
    if cpf in usuarios:
        print('CPF já cadastrado. Não é permitido cadastrar novamente.')
        return
    usuarios[cpf] = {'nome': nome, 'dt_nascimento': dt_nascimento, 'cpf': cpf, 'endereco': endereco}
    print('Usuário cadastrado com sucesso.')


def cadastrar_conta(): 
    agencia = '0001'  
    numero_conta = input('Digite o número da conta: ')
    cpf = input('Digite o CPF do usuário: ')
    if cpf not in usuarios:
        print('CPF não cadastrado. Cadastre o usuário primeiro.')
        return
    usuarios[cpf]['contas'].append({'agencia': agencia, 'numero_conta': numero_conta})
    print('Conta cadastrada com sucesso.')

 
def menu_conta():   
    print('#####################SEJA BEM VINDO AO SISTEMA DE CADASTRO DE CLIENTE E CONTA #######################################')
    while True:
        opcao = int(input("0-PARA SAIR \n 1-PARA CADASTRAR UM USUÁRIOS \n 2-PARA CRIAR UMA CONTA"))
        match opcao:
            case 0: return False
            case 1: cadastrar_usuario()
            case 2: cadastrar_conta()
            case _: print('Comando Inválido')
        
