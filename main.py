# -*-coding:Latin-1 -*
import os
import random
import math


def InputInt(text):
    test = input(text)
    while not test.isdigit():
        print("La valeure saisie est incorrecte")
        test: str = input(text)
    return int(test)


def SameParity(a, b):
    if a % 2 == b % 2:
        return True
    else:
        return False


pot = 100
gain = 0


while True:
    print("Votre pot actuel est de : ", pot, '$')

    choix = InputInt("Sur quel nombre souhaitez vous miser (entre 0 et 49 : ")
    if choix > 49:
        print("Le nombre choisi n'est pas valable")
        continue

    mise = InputInt("Combien souhaitez vous miser : ")
    if mise <= pot:
        resultat = random.randrange(50)
        if choix == resultat:
            gain = 3 * mise
        elif SameParity(choix, resultat):
            gain = math.ceil(mise / 2)
        else:
            gain = 0
        print("Le résultat de la roulette est ", resultat, " Vous avez gagné :", gain, ("$"))
        pot = pot - mise + gain

    else:
        print("Votre mise est trop élevé coup annulé")
