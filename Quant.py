import os 


os.system("cls || clear")

pares = 0
impares = 0
mediaGeral = 0
contadadroGeral = 0
somaGeral = 0

numero = 0

somaGeral+=numero
contadadroGeral+=1

while numero == 0:
    numero = int(input("Digite um número:"))
    
    if numero %2 == 0 and numero > 0:
     pares+=1
    elif numero %2 !=0 and numero>0:
     impares+=1


print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números impares: {impares}")
print(f"Quantidade de todos os números: {contadadroGeral}")

     
