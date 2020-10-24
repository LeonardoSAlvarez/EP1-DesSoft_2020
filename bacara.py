# EP - Design de Software
# Equipe: Leonardo Alvarez
# Data: 23/10/2020

import random
import math

baralho=['A',2,3,4,5,6,7,8,9,10,'J','Q','K']

somaj = 0
somab = 0

resultado = 0

gameon = False

#fichas iniciais
fichas = 100
aposta = 0

#comeco do jogo
print("Você tem: 100 fichas")
print('  ')
print('Para sair do jogo digite: "desligar" no inicio da rodada.')

pergunta = input("Você quer começar o jogo? (sim/não)")

if pergunta == "sim" or pergunta == "s" or pergunta == "Sim":
    gameon = True

while gameon == True and fichas != 0:
    print('  ')
    print('---------------------------')
    print("Início da rodada.")

    dj = 0
    db = 0

#para apostar
    quem = input('Em quem quer apostar? (jogador/banco/empate)')
    if quem != 'desligar':
        aposta = int(input("Quanto você quer apostar?"))

#desligar
    
        
        
 #randomiza carta       
        cj1 = random.choice(baralho)
        cj2 = random.choice(baralho)

        cb1 = random.choice(baralho)
        cb2 = random.choice(baralho)

    #valor da carta
        if cj1 == 'A':
            cj1 = 1
        elif cj1 == 10 or cj1 == 'J' or cj1 == 'Q' or cj1 == 'K':
            cj1 = 0
        else:
            cj1 = cj1

        if cj2 == 'A':
            cj2 = 1
        elif cj2 == 10 or cj2 == 'J' or cj2 == 'Q' or cj2 == 'K':
            cj2 = 0
        else:
            cj2 = cj2

        if cb1 == 'A':
            cb1 = 1
        elif cb1 == 10 or cb1 == 'J' or cb1 == 'Q' or cb1 == 'K':
            cb1 = 0
        else:
            cj1 = cj1

        if cb2 == 'A':
            cb2 = 1
        elif cb2 == 10 or cb2 == 'J' or cb2 == 'Q' or cb2 == 'K':
            cb2 = 0
        else:
            cb2 = cb2

    #somas iniciais
        somaj = cj1 + cj2
        somab = cb1 + cb2



        if somaj == 8 or somaj == 9:
            if somab == 8 or somab == 9:
                resultado = 'e'
            else:
                resultado = 'j'

        elif somab == 8 or somab == 9:
            resultado = 'b'
            
        else:

    #analise da soma inicial 
                
            if somaj >= 10 and somaj < 20:
                somaj -= 10
            elif somaj >= 20:
                somaj -= 20

            if somab >= 10 and somab < 20:
                somab -= 10
            elif somab >= 20:
                somab -= 20

            #se precisar 3 cartas j
            if somaj <= 5:
                cj3 = random.choice(baralho)

                if cj3 == 'A':
                    cj3 = 1
                elif cj3 == 10 or cj3 == 'J' or cj3 == 'Q' or cj3 == 'K':
                    cj3 = 0
                else:
                    cj3 = cj3

                somaj = cj1 + cj2 + cj3

                if somaj >= 10 and somaj < 20:
                    somaj -= 10
                elif somaj >= 20:
                    somaj -= 20

            #se precisar 3 cartas b
            if somab <= 5:
                cb3 = random.choice(baralho)

                if cb3 == 'A':
                    cb3 = 1
                elif cb3 == 10 or cb3 == 'J' or cb3 == 'Q' or cb3 == 'K':
                    cb3 = 0
                else:
                    cb3 = cb3

                somab = cb1 + cb2 + cb3

                if somab >= 10 and somab < 20:
                    somab -= 10
                elif somab >= 20:
                    somab -= 20


            #analise da soma final
            if somaj == 8 or somaj == 9:
                if somab == 8 or somab == 9:
                    resultado = 'e'
                else:
                    resultado = 'j'

            elif somab == 8 or somab == 9:
                resultado = 'b'

            elif somaj == somab:
                resultado = 'e'
            else:
                dj = 8 - somaj
                db = 8 - somab
                if dj < db:
                    resultado = 'j'
                else:
                    resultado = 'b'





        print('')
        print("A soma do jogador deu: {0}".format(somaj))
        print('')
        print("A soma do banco deu: {0}".format(somab))


        #fichas
        if resultado == 'j' and quem == 'jogador':
            fichas += aposta
        elif resultado == 'b' and quem == 'banco':
            fichas += math.floor(0.95 * aposta)
        elif resultado == 'e' and quem == 'empate':
            fichas += aposta * 8
        else:
            fichas -= aposta

    
        print("Voce tem: {0} fichas.".format(fichas))


    else:
        gameon = False
    
    

else:
    print('')
    print("O jogo acabou!")
    print("Voce terminou com {0} fichas".format(fichas))
