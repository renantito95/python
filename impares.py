n = int(input("Digite um numero inteiro positivo: "))

# Iniciado as variaveis
contagem_impares = 0
num = 1

# Loop
while contagem_impares < n:
    if num % 2 != 0:
        print(num)
        contagem_impares +=1
    num += 1