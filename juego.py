# adivina el número
import random

IntentosRealizados = 0

Número = random.randint(0,40)
print("HOLA, el juego consiste en adivinar el número que estoy pensando. Tienes 5 intentos y el número se encuentra entre el 0 y el 40")

while IntentosRealizados < 5:
    Respuesta = input()
    Respuesta = int(Respuesta)
    
    IntentosRealizados = IntentosRealizados + 1

    if Respuesta < Número:
        print("Elige un número más alto")

    if Respuesta > Número:
        print("Elige un número más bajo")

    if Respuesta == Número:
        break

if Respuesta == Número:
    IntentosRealizados = str(IntentosRealizados)
    print("Lo lograste, has adivinado el número en " + IntentosRealizados + " intentos")

if Respuesta != Número:
    Número = str(Número)
    print("Perdiste, no adivinaste el número. El número correcto era " + Número)