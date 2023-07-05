import random

def evaluar(original, individuo):
    puntuacion = 0
    for i in range(len(original)):
        puntuacion += 1 if original[i] == individuo[i] else 0
    return puntuacion/len(original)

def generar_individuo(longitud):
    palabra = ""
    for _ in range (longitud):
        palabra += chr(random.randint(97,122))
    return palabra

def cruza(cadena1, cadena2):
    punto_cruza = random.randint(0, len(cadena1))
    cadena_hijo1 = cadena1[0:punto_cruza] + cadena2[punto_cruza:]
    cadena_hijo2 = cadena2[0:punto_cruza] + cadena1[punto_cruza:]
    return cadena_hijo1, cadena_hijo2

def mutacion(cadena, prob_mutar):
    cadena_mutada = list(cadena)
    for i in range (len(cadena)):
        cadena_mutada[i] = chr(random.randint(97,122)) if random.random() < prob_mutar else cadena_mutada[i]
    return "".join(cadena_mutada)

def crear_poblacion(tamano, original):
    poblacion = []
    for _ in range(tamano):
        palabra = generar_individuo(len(original))
        poblacion.append(
            {
                "cadena": palabra,
                "aptitud": evaluar(original, palabra)
            }
        )
    return poblacion

def seleccion_padres(poblacion):
    padres = []
    while len(padres) < len(poblacion):
        for individuo in poblacion:
            fit = 0.1 if individuo["aptitud"] == 0 else individuo["aptitud"]
            if random.random() < fit:
                padres.append(individuo)
    return padres

def estadisticas(poblacion):
    mejor = poblacion[0]
    peor = poblacion[0]
    suma_fit = 0
    for individuo in poblacion:
        mejor = individuo if individuo["aptitud"] >= mejor["aptitud"] else mejor
        peor = individuo if individuo["aptitud"] <= peor["aptitud"] else peor
        suma_fit += individuo["aptitud"]
    return mejor, peor, suma_fit/len(poblacion)

prob_cruza = 1.0
prob_mutar = 0.1
generaciones = 100
tam_pop = 100
objetivo = "holamundo"

poblacion = crear_poblacion(tam_pop, objetivo)
for g in range(generaciones):
    mejor, peor, prom_fit = estadisticas(poblacion)
    print("{:.0f} {} {:.2f} {:.2f}".format(g, mejor["cadena"],mejor["aptitud"], prom_fit))

    if(mejor["aptitud"]== 1):
        break

    padres = seleccion_padres(poblacion)

    siguiente_generacion =[]
    for p in range(0, tam_pop, 2):
        hijo1 = {}
        hijo2 = {}
        if random.random() < prob_cruza:
            cadena_hijo1, cadena_hijo2 = cruza(padres[p]["cadena"], padres[p+1]["cadena"])
            hijo1 = {"cadena": cadena_hijo1, "aptitud":0}
            hijo2 = {"cadena": cadena_hijo2, "aptitud":0}
            #print(p, hijo1, hijo2)
        else:
            hijo1 = padres[p]
            hijo2 = padres[p+1]
        hijo1["cadena"] = mutacion(hijo1["cadena"], prob_mutar)
        hijo2["cadena"] = mutacion(hijo2["cadena"], prob_mutar)
        hijo1["aptitud"] = evaluar(objetivo, hijo1["cadena"])
        hijo2["aptitud"] = evaluar(objetivo, hijo2["cadena"])
        siguiente_generacion.append(hijo1)
        siguiente_generacion.append(hijo2)
    poblacion  = siguiente_generacion
    poblacion[0] = mejor
print(estadisticas(poblacion))