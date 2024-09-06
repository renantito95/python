n = int(input("Digite um numero: "))
primo = 0

for i in range (1 , (n + 1)):
    if n % i == 0:
        primo += 1

if primo == 2:
    print("Primo")
else:
    print("não primo")

 
