import os 

os.system("cls || clear")
opcao = 1

while opcao != 0: 
    print("*Código*  |    *Descrição*") 
    print("   1    |    Adicionar pessoa")
    print("   2    |    Exibir resultados e sair")

    opcao = int(input("Escolha uma das opções:"))
    quant = int(input("Deseja adicionar quantas pessoas?"))

    match (opcao):
        case 1: 
          for i in range (quant): 
           print("\n")
           print(f"{i + 1}ª pessoa")
           idade = int(input("Digite sua idade:"))
           sexo = str(input("Digite seu sexo (M/F):"))
           salario = float(input("Digite seu salário:"))
           
        case 2:
           print("\n")
           print(f"{i + 1}ª pessoa")
           print (f"Idade:")
           print (f"Sexo (M/F):")
           print (f"Salário:")
            
 

        