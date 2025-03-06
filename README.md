# Sistema Bancário Simples

Este projeto foi desenvolvido como parte de um curso na plataforma DIO (Digital Innovation One). O objetivo é criar um sistema bancário simples que permite o cadastro de usuários, criação de contas e operações bancárias básicas como depósito, saque e consulta de extrato.

## Estrutura do Projeto
O projeto é composto por quatro arquivos principais:

- **cliente.py**: Contém as funções para cadastrar usuários e contas.
- **menu_conta.py**: Gerencia o menu de cadastro de usuários e contas.
- **sistema.py**: Gerencia as operações bancárias como depósito, saque e extrato.
- **menu_sistema.py**: Gerencia o menu de operações bancárias.

## Funcionalidades

### cliente.py
Este arquivo contém as seguintes funções:

- `cadastrar_usuario()`: Cadastra um novo usuário no sistema.
- `cadastrar_conta()`: Cadastra uma nova conta para um usuário existente.

### menu_conta.py
Este arquivo contém a função `menu_conta()`, que exibe um menu para o usuário escolher entre cadastrar um novo usuário ou criar uma nova conta.

### sistema.py
Este arquivo contém as seguintes funções:

- `depositar()`: Realiza um depósito na conta do usuário.
- `extrato()`: Exibe o extrato bancário, mostrando os saques e depósitos realizados, além do saldo atual.
- `saque()`: Realiza um saque na conta do usuário, respeitando o limite diário de saques e o valor máximo por saque.

### menu_sistema.py
Este arquivo contém a função `menu()`, que exibe um menu para o usuário escolher entre realizar um depósito, consultar o extrato ou realizar um saque.

## Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone [https://github.com/seu-usuario/sistema-bancario-simples.git](https://github.com/Luamateus2/Projeto-Dio.git)
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd projeto-dio
   ```
3. Execute o menu de contas:
   ```bash
   python menu_conta.py
   ```
4. Execute o menu de operações bancárias:
   ```bash
   python menu_sistema.py
   ```

## Requisitos
- Python 3.x

## Exemplo de Uso

### Cadastrar um usuário:
1. Execute `menu_conta.py`.
2. Escolha a opção 1 para cadastrar um novo usuário.
3. Insira os dados solicitados (nome, data de nascimento, CPF, endereço).

### Criar uma conta:
1. Escolha a opção 2 para criar uma nova conta.
2. Insira o número da conta e o CPF do usuário.

### Realizar operações bancárias:
1. Execute `menu_sistema.py`.
2. Escolha a opção 1 para depositar, 2 para consultar o extrato ou 3 para sacar.


## Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

**Nota:** Este projeto foi desenvolvido como parte de um curso na plataforma DIO e tem fins educacionais.

✍️ Autor

Feito por Luana Karoline. Para contato, envie um e-mail para luanakarolineliramateus2021@gmail.com.
