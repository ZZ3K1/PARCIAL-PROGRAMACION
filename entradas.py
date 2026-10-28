import salidas


def validar_entero_no_negativo(texto):
    """Valida que un texto represente un entero mayor o igual a cero

    Args:
        texto (str): Texto ingresado por el usuario

    Returns:
        bool: True si el texto tiene solo digitos, False en caso contrario
    """
    es_valido = len(texto) > 0
    for caracter in texto:
        if caracter < "0" or caracter > "9":
            es_valido = False
    return es_valido


def pedir_entero_no_negativo(mensaje):
    """Pide un entero no negativo y reintenta hasta que sea valido

    Args:
        mensaje (str): Texto que se muestra al pedir el dato

    Returns:
        int: Numero entero mayor o igual a cero
    """
    texto = input(mensaje)
    while not validar_entero_no_negativo(texto):
        salidas.mostrar_error(
            "Dato invalido. Ingrese un entero mayor o igual a 0 "
            "(sin letras ni negativos)"
        )
        texto = input(mensaje)
    return int(texto)


def pedir_opcion_menu(minimo, maximo):
    """Pide una opcion del menu dentro de un rango valido

    Args:
        minimo (int): Menor opcion permitida
        maximo (int): Mayor opcion permitida

    Returns:
        int: Opcion elegida dentro del rango
    """
    opcion = pedir_entero_no_negativo("\nSeleccione una opcion: ")
    while opcion < minimo or opcion > maximo:
        salidas.mostrar_error(f"Opcion fuera de rango ({minimo}-{maximo}).")
        opcion = pedir_entero_no_negativo("Seleccione una opcion: ")
    return opcion


def cargar_votos_secuencial(votos_partidos, cantidad_partidos):
    """Carga de forma secuencial los votos de cada partido

    Args:
        votos_partidos (list): Lista donde se guardan los votos
        cantidad_partidos (int): Cantidad de partidos a cargar

    Returns:
        list: La misma lista con los votos cargados
    """
    for i in range(cantidad_partidos):
        mensaje = f"Votos del partido {i + 1}: "
        cantidad = pedir_entero_no_negativo(mensaje)
        votos_partidos.append(cantidad)
    return votos_partidos
