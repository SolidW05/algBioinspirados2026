import random

OBJETIVO = 200
TAMANO_POBLACION = 8
RONDAS = 80


# Menor error = mejor solución.
def calcular_error(numero):
    resultado = numero * numero
    return abs(OBJETIVO - resultado)


def ejecutar_algoritmo():

    poblacion = [
        random.uniform(0, 200)
        for _ in range(TAMANO_POBLACION)
    ]

    print("OBJETIVO: encontrar un número cuyo cuadrado sea", OBJETIVO)
    print("Población inicial:", poblacion)

    for ronda in range(1, RONDAS + 1):

        poblacion.sort(key=calcular_error)

        mejor = poblacion[0]

        print("\nRonda", ronda)
        print("Población ordenada:", poblacion)
        print("Mejor número:", mejor)
        print("Resultado:", mejor * mejor)
        print("Error:", calcular_error(mejor))

        if calcular_error(mejor) == 0:
            print("\n¡Encontramos una solución exacta!")
            return mejor

        seleccionados = poblacion[:3]

        print("Seleccionados:", seleccionados)

        clones_modificados = []

        for posicion, numero in enumerate(seleccionados):

            # El mejor produce más copias.
            cantidad_copias = (3 - posicion) * 2

            cambio_maximo = posicion + 1

            for _ in range(cantidad_copias):

                cambio = random.randint(
                    -cambio_maximo,
                    cambio_maximo
                )

                clon = numero + cambio

                clon = max(0, min(200, clon))

                clones_modificados.append(clon)

        print("Copias modificadas:", clones_modificados)

        candidatos = poblacion + clones_modificados
        candidatos.sort(key=calcular_error)

        nueva_poblacion = candidatos[:TAMANO_POBLACION - 1]

        nueva_poblacion.append(random.uniform(0, 200))

        poblacion = nueva_poblacion

    mejor = min(poblacion, key=calcular_error)

    print("\nTerminaron las rondas.")
    print("Mejor número encontrado:", mejor)
    print("Resultado:", mejor * mejor)
    print("Error:", calcular_error(mejor))

    return mejor


ejecutar_algoritmo()