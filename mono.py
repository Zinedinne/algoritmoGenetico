import random

def cajanegra(entrada):
    secreta = "holamundo"
    puntuacion = 0
    for i in range(len(secreta)):
        puntuacion += 1 if secreta[i] == entrada[i] else 0
    return puntuacion/len(secreta)

def mono(longitud):
    palabra = ""
    for _ in range (longitud):
        palabra += chr(random.randint(97,122))
    return palabra

#print(cajanegra("holabolas"))

g=0
while(True):
    palabra = mono (9)
    puntuacion = cajanegra(palabra)
    print(g, palabra, puntuacion)
    if puntuacion == 1:
        break
    g+=1

