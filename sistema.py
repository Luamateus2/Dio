#só depositar numeros positivos
#remover o array para nome
#não pode depositar numero negativo
nome= input('Digite o seu nome: ')
saldo= float(input("Digite seu saldo inicial : "))
depositados = []
retiradas = []
op=1
while(op!=0):
   op= int(input("0-SAI\n1-DEPOSITAR\n2-EXTRATO\n3-SAQUE\n"))
   if(op==1):
       valor=float(input("Qual o valor que deseja depositar? "))
       if(valor<=0):
           print("Não é possível depositar valor negativo")
       else:
           saldo+=valor 
           depositados.append(valor)
           print("Depositado com sucesso!")
   elif(op==2):
        print(f"SR(A){nome} seu extrato:")
        print(f'Saques realizados: {retiradas}')
        print(f'Depositos realizados: {depositados}')
        print(f"Saldo : R${saldo}")
        
        
   elif(op==3):
     dia=0
     if(dia<3):  
        saque = float(input("Digite o valor a ser sacado: "))
        if(saque<=500 ):
            if(saque>saldo or saque<0):
                print("Saldo Insuficiente ou Valor inválido!")
            else:
                saldo-=saque
                retiradas.append(saque)
                dia+=1
                print("Saque realizado com sucesso")
        else:
            print('Não pode retirar valores maiores que R$500')        
     else:
         print("Não é possível realizar mais nenhum saque")       
            
                 
       
