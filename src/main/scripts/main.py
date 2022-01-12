def pedir_valor(frase_mostrar, tipo):
    entrada = ""
    valor_correcto = False
    while not valor_correcto:
        entrada = input(frase_mostrar)
        if isinstance(tipo, list):
            # como el tipo es una lista miramos si esta en los valores
            if entrada in tipo:
                valor_correcto = True
            else:
                valor_correcto = False
        else:
            valor_correcto = revisar_valor(tipo, entrada)
        if not valor_correcto:
            print("El valor introducido no es correcto.")
    return entrada


def revisar_valor(tipo, entrada):
    valor_correcto = False
    try:
        if tipo == "letra" and len(entrada) == 1 and entrada.isalpha():
            valor_correcto = True
        elif tipo == "numero":
            int(entrada)
            valor_correcto = True
        elif tipo == "palabra" and ' ' not in entrada:
            valor_correcto = True
        elif tipo == "frase" and ' ' in entrada and len(entrada.split(
                ' ')) > 1:
            valor_correcto = True
    except ValueError:
        valor_correcto = False

    return valor_correcto


def tratar_letra_encontrada(letra_insertada, frase_partida, letras_adivinadas):
    for contPalabras in range(len(frase_partida)):
        for contadorLetras in range(len(frase_partida[contPalabras])):
            if frase_partida[contPalabras][contadorLetras].lower() == \
                    letra_insertada.lower():
                letras_adivinadas[contPalabras][contadorLetras] \
                    = frase_partida[contPalabras][contadorLetras]


def generar_letras_adivinadas_frase_partida(frase_introducida,
                                            letras_adivinadas,
                                            frase_partida):
    for palabra in frase_introducida.split():
        letras_adivinadas.append(["+" for x in palabra])
        frase_partida.append([f"{x}" for x in palabra])


def dame_cadena_concatenada(lista, separador):
    resultado = ""
    if len(lista) > 0:
        for valor in lista:
            resultado += str(valor) + separador
        return resultado[:-2]
    else:
        return ""


def adivinar_numero_palabras(contador, cantidad, intentos_numero, frase):
    encontrado = False
    while contador <= cantidad and not encontrado:
        contador += 1
        num_insertado = pedir_valor("adivine número de palabras: ", "numero")

        intentos_numero.append(num_insertado)
        if int(num_insertado) == len(frase.split(' ')):
            print(f"Has acertado el número! La frase tiene "
                  f"{len(frase.split(' '))} palabras:")
            encontrado = True
        elif int(num_insertado) > len(frase.split(' ')):
            print(f"Intento erróneo. El número a adivinar es menor. "
                  f"{cantidad - contador + 1} intentos disponibles.")
        else:
            print(f"Intento erróneo. El número a adivinar es mayor. "
                  f"{cantidad - contador + 1} intentos disponibles.")
    return contador


def adivinar_letra(intentos_letras, frase, frase_partida, letras_adivinadas,
                   cantidad, contador):
    letra_insertada = pedir_valor("adivine letra: ", "letra")

    intentos_letras.append(letra_insertada)
    if letra_insertada.lower() in frase.lower():
        # Letra encontrada
        tratar_letra_encontrada(letra_insertada, frase_partida,
                                letras_adivinadas)

        print("Intento correcto. Existe la letra. " + ' '.join(
            [''.join(lst) for lst in letras_adivinadas]) +
              f". {cantidad - contador + 1} intentos disponibles.")
    else:
        # letra no encontrada
        print("Intento erróneo. No existe la letra. " + ' '.join(
            [''.join(lst) for lst in letras_adivinadas]) +
              f". {cantidad - contador + 1} intentos disponibles.")


def adivinar_palabra(intentos_palabras, frase, frase_partida,
                     letras_adivinadas, cantidad, contador):
    palabra_insertada = pedir_valor("adivine palabra: ", "palabra")

    intentos_palabras.append(palabra_insertada)
    if palabra_insertada.lower() in frase.lower().split(' '):
        # Palabra encontrada
        indice = \
            frase.lower().split(' ').index(
                palabra_insertada.lower())

        for contLetras in range(len(frase_partida[indice])):
            letras_adivinadas[indice][contLetras] = \
                frase_partida[indice][contLetras]

        print("Intento correcto. Existe la palabra. " + ' '.join(
            [''.join(lst) for lst in letras_adivinadas]) +
              f". {cantidad - contador + 1} intentos disponibles.")
    else:
        # letra no encontrada
        print("Intento erróneo. No existe la palabra. " + ' '.join(
            [''.join(lst) for lst in letras_adivinadas]) +
              f". {cantidad - contador + 1} intentos disponibles.")


def adivinar_frase(intentos_frases, frase, letras_adivinadas, cantidad,
                   contador):
    frase_insertada = pedir_valor("adivine frase: ", "frase")
    intentos_frases.append(frase_insertada)
    if frase_insertada.lower() == frase.lower():
        # frase Acertada
        print("Ha acertado la frase!")
        encontrada_frase = True
    else:
        # Frase Errónea
        print("Intento erróneo. No has acertado la frase. "
              "Palabras adivinadas "
              + ' '.join([''.join(lst) for lst in
                          letras_adivinadas]) +
              f". {cantidad - contador + 1} intentos disponibles.")
        encontrada_frase = False

    return encontrada_frase


def jugar():
    frase = pedir_valor("introduzca frase: ", "frase")
    cantidad = int(pedir_valor("introduzca intentos permitidos: ", "numero"))

    contador = 1
    encontrada_frase = False
    intentos_numero = []
    intentos_letras = []
    intentos_palabras = []
    intentos_frases = []
    letras_adivinadas = []
    frase_partida = []

    generar_letras_adivinadas_frase_partida(frase, letras_adivinadas,
                                            frase_partida)

    # --------------- Numero de palabras ----------
    contador = adivinar_numero_palabras(contador, cantidad, intentos_numero,
                                        frase)

    # --------------- Búsqueda frase ----------
    # Cantidad palabras acertada, ahora la parte de las letras
    while contador <= cantidad and not encontrada_frase:
        contador += 1
        tipo_eleccion = int(
            pedir_valor("adivine letra introduzca "
                        "2\nadivine palabra introduzca "
                        "1:\nadivine frase introduzca 0:\n",
                        ["0", "1", "2"]))

        if tipo_eleccion == 2:
            # --- Adivinar letra ---
            adivinar_letra(intentos_letras, frase, frase_partida,
                           letras_adivinadas, cantidad, contador)

        elif tipo_eleccion == 1:
            # --- Adivinar palabra ---
            adivinar_palabra(intentos_palabras, frase, frase_partida,
                             letras_adivinadas, cantidad, contador)

        else:
            # --- Adivinar frase ---
            encontrada_frase = adivinar_frase(intentos_frases, frase,
                                              letras_adivinadas, cantidad,
                                              contador)

    print("Los intentos numero de letras fueron los siguientes: " +
          dame_cadena_concatenada(intentos_numero, ", ") + '.')
    print("Los intentos de letras fueron los siguientes: " +
          dame_cadena_concatenada(intentos_letras, ", ") + '.')
    print("Los intentos de palabras fueron los siguientes: " +
          dame_cadena_concatenada(intentos_palabras, ", ") + '.')
    print("Los intentos de frase fueron los siguientes: " +
          dame_cadena_concatenada(intentos_frases, ", ") + '.')

    if encontrada_frase:
        return 1
    else:
        return 0


if __name__ == "__main__":
    jugar()
