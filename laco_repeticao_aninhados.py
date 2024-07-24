# Parte crescente
for i in range(1, 6):
    for j in range(1, i + 1):
        print('*', end= ' ')
    print()
# i representa o numero da linha atual, que tbm corresponde ao numero de estrelas a serem impressas nessa linha
# j representa a posição atual na linha, e controla quantas estrelas são impressas.


# Parte decrescente
for i in range(4, 0, -1):
    for j in range(1, i + 1):
        print('*', end=' ')
    print()