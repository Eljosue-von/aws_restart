import random

numero = random.randint(1,10)

print("numero aleatorio generado entre 1 y 10 es: " + str(numero))

estaAdivinado = False
while estaAdivinado != True:
    numeroDigitado = input("Ingresa el numero entre 1 y 10 ")
    if int(numeroDigitado) == numero:
        print("adivinaste, el numero es {}. Ganaste!".format(numeroDigitado))
        estaAdivinado = True
    else:
        print("Tu numero fue {}. Lo sinto, ese no es el numero intnta de nueva".format(numeroDigitado))

