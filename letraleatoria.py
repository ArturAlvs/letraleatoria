import string
import random
# gera uma letra random
letra_random = random.choice(string.ascii_lowercase[:-1])
# usa ela como letra do jogador
letra_jogador = letra_random
print("A letra é: {}".format(letra_jogador))
# enquanto nao terminou
while letra_jogador < 'z':
	letra_jogador = input("Digite a proxima letra: ")
# print("Voce ganhou!")
i = input("Voce ganhou!")