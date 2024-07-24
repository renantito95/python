numero = float(input('Digite um número para saber se é par ou impar: '))
resto = numero % 2

if resto == 0:
    print('Numero é par')
else:
    print('Numero é impar')