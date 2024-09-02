print ("Bem vindo ao nosso programa em python")
print ("-"*30)
print ("MMC")
print ("-"*30)

num1 = int(input("Digite um numero inteiro: "))
num2 = int(input("Digite outro numero inteiro: "))

if num1 > num2:
    maior = num1

else:
    maior = num2

while True:
    if maior % num1 == 0 and maior % num2 == 0:
        print (maior)
        break
    else:
        maior += 1