import zipfile
import random

print("********************************")
print("Bem-vindo ao jogo de adivinhacão")
print("********************************")

numero_secreto = random.randint(0,100)
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas):
    chute_str = input("Digite o numero: ")
    chute = int(chute_str)
    print("Voce digitou ", chute_str)
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Voce acertou")
        break
    else:
        if(maior):
            print("Tente um numero menor")
        elif(menor):
            print("Tente um numero maior")

    rodada = rodada + 1
    continue

print("Você não conseguiu. Total de rodadas: {}".format(rodada))
