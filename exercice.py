#!/usr/bin/env python
import math


def dissipated_power(voltage, resistance):
    # TODO: Calculer la puissance dissipée par la résistance.
    return pow(voltage, 2) / resistance


def orthogonal(v1, v2):
    # TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
    v1[0]  # Pour accéder au X
    v1[1]  # Pour accéder au Y
    isOrthogonaux = None
    if v1[0] * v2[0] + v1[1] * v2[1] == 0:
        isOrthogonaux = True
    else:
        isOrthogonaux = False

    return isOrthogonaux


def average(values):
    # TODO: Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives).

    cpt = total = 0

    for v in values:
        if v > 0:
            total += v
            cpt += 1

    moyenne = total / cpt

    return moyenne


def bills(value):
    # TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur.
    twenties = tens = fives = twos = ones = 0
    while value != 0:
        if value >= 20:
            value = value - 20
            twenties += 1
        elif value >= 10:
            value = value - 10
            tens += 1
        elif value >= 5:
            value = value - 5
            fives += 1
        elif value >= 2:
            value = value - 2
            twos += 1
        elif value >= 1:
            ones = value
            value = 0

    return (twenties, tens, fives, twos, ones);


if __name__ == "__main__":
    print(dissipated_power(69, 420))
    print(orthogonal((1, 1), (-1, 1)))
    print(average([1, 4, -2, 10]))
    print(bills(137))
