numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
numero3 = int(input("Digite o terceiro numero: "))
numero4 = int(input("Digite o quarto numero: "))

x1 = numero1
x2 = numero2
y1 = numero3
y2 = numero4

distancia = (x1 - x2) ** 2 + (y1 - y2) ** 2

if distancia >= 10:
    print("Longe")
else:
    print("perto")
