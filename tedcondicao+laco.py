import random
numero = 0
palpite = 0
numero = random.choice(list(range(1, 100)))
tentativas = 0
print("\nUm número foi gerado, descubra qual ;)")
while numero != palpite:
    palpite = int(input("\nDigite o numero que você acha que foi gerado: "))
    tentativas += 1
    if numero > palpite:
        print("Seu palpite foi abaixo do numero")
    elif numero < palpite:
        print("Seu palpite foi acima do numero")
    else:
        print("\nAcertou, em ", tentativas,"tentavivas você descobriu o numero.")




