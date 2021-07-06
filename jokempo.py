from random import randint
fim = 10
cont = 0
p1 = 0
e = 0
p2 = 0
while cont < fim:
    jogo = ("pedra", "papel", "tesoura")

    player1 = int(input('''JOKENPO: 
    [ 0 ] pedra
    [ 1 ] papel
    [ 2 ] tesoura ? '''))

    player2 = randint(0, 2)

    print("player1 escolheu: {}" .format(jogo[player1]) )
    print("player2 escolheu: {}" .format(jogo[player2]) )

    if player1 == 0:
        if player2 == 0:
            print("EMPATE")
            e += 1
        elif player2 == 1:
            print("player2 venceu")
            p2 += 1
        elif player2 == 2:
            print("player1 venceu")
            p1 += 1
        else:
            print("Fim do jogo")

    elif player1 == 1:
        if player2 == 0:
            print("player1 venceu")
            p1 += 1
        elif player2 == 1:
            print("EMPATE")
            e += 1
        elif player2 == 2:
            print("player2 venceu")
            p2 += 1
        else:
            print("Fim do jogo")

    elif player1 == 2:
        if player2 == 0:
            print("player2 venceu")
            p2 += 1
        elif player2 == 1:
            print("player1 venceu")
            p1 += 1
        elif player2 == 2:
            print("EMPATE")
            e += 1
    cont = cont + 1

print(f"player1 venceu {p1} vezes")
print(f"player2 venceu {p2} vezes")
print(f"empate {e} vezes")

if p1 == p2 :
    print("empate")
elif p1 > p2:
        print("player 1 venceu")
else:
        print("player 2 venceu")













 
