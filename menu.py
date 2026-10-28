import entradas
import funciones
import salidas

CANTIDAD_PARTIDOS = 5


def listar_partidos(votos_partidos, indices):
    """Muestra votos y porcentaje de los partidos indicados

    Args:
        votos_partidos (list): Votos de cada partido
        indices (list): indices de los partidos a mostrar

    Returns:
        int: Cantidad de partidos mostrados
    """
    total = funciones.calcular_suma(votos_partidos)
    for i in range(len(indices)):
        indice = indices[i]
        porcentaje = funciones.calcular_porcentaje(
            votos_partidos[indice], total
        )
        salidas.mostrar_partido(indice, votos_partidos[indice], porcentaje)
    return len(indices)


def cargar_votos_partidos(votos_partidos):
    """Opcion 1: carga los votos de los partidos (reemplaza lo anterior)

    Args:
        votos_partidos (list): Lista donde se guardan los votos

    Returns:
        list: La lista con los votos cargados
    """
    funciones.limpiar_lista(votos_partidos)
    salidas.mostrar_titulo("Carga de votos")
    entradas.cargar_votos_secuencial(votos_partidos, CANTIDAD_PARTIDOS)
    salidas.mostrar_mensaje("Votos cargados correctamente")
    return votos_partidos


def informar_votos_partidos(votos_partidos):
    """Opcion 2: muestra todos los partidos con su porcentaje

    Args:
        votos_partidos (list): Votos de cada partido

    Returns:
        int: Cantidad de partidos mostrados
    """
    salidas.mostrar_titulo("Listado de votos")
    indices = []
    for i in range(len(votos_partidos)):
        indices.append(i)
    listar_partidos(votos_partidos, indices)
    total = funciones.calcular_suma(votos_partidos)
    salidas.mostrar_resumen_general(len(votos_partidos), total)
    return len(indices)


def informar_menores_porcentaje(votos_partidos, limite):
    """Opciones 3, 4 y 5: partidos con menos de un porcentaje de votos

    Args:
        votos_partidos (list): Votos de cada partido
        limite (int): Porcentaje limite (exclusivo)

    Returns:
        int: Cantidad de partidos encontrados
    """
    salidas.mostrar_titulo(f"Partidos con menos del {limite}% de votos")
    indices = funciones.buscar_indices_menores_porcentaje(
        votos_partidos, limite
    )
    if len(indices) == 0:
        salidas.mostrar_error(
            f"Ningun partido tiene menos del {limite}% de los votos"
        )
    else:
        listar_partidos(votos_partidos, indices)
        acumulado = funciones.calcular_porcentaje_acumulado(
            votos_partidos, indices
        )
        salidas.mostrar_porcentaje_acumulado(acumulado)
    return len(indices)


def informar_mayores_votos(votos_partidos, limite):
    """Opciones 6 y 7: partidos con mas votos que un limite

    Args:
        votos_partidos (list): Votos de cada partido.
        limite (int): Cantidad de votos limite (exclusiva)

    Returns:
        int: Cantidad de partidos encontrados
    """
    salidas.mostrar_titulo(f"Partidos con mas de {limite} votos")
    indices = funciones.buscar_indices_mayores_votos(votos_partidos, limite)
    if len(indices) == 0:
        salidas.mostrar_error(f"Ningun partido tiene mas de {limite} votos")
    else:
        listar_partidos(votos_partidos, indices)
        suma = funciones.calcular_votos_por_indices(votos_partidos, indices)
        promedio = funciones.calcular_promedio(suma, len(indices))
        salidas.mostrar_resumen_busqueda(suma, len(indices), promedio)
    return len(indices)


def informar_sobre_promedio(votos_partidos):
    """Opcion 8: partidos por encima del promedio general de votos

    Args:
        votos_partidos (list): Votos de cada partido

    Returns:
        int: Cantidad de partidos encontrados
    """
    salidas.mostrar_titulo("Partidos por encima del promedio")
    total = funciones.calcular_suma(votos_partidos)
    promedio = funciones.calcular_promedio(total, len(votos_partidos))
    salidas.mostrar_promedio_general(promedio)
    indices = funciones.buscar_indices_sobre_promedio(votos_partidos)
    if len(indices) == 0:
        salidas.mostrar_error("Ningun partido supera el promedio general")
    else:
        listar_partidos(votos_partidos, indices)
        acumulado = funciones.calcular_porcentaje_acumulado(
            votos_partidos, indices
        )
        salidas.mostrar_porcentaje_acumulado(acumulado)
    return len(indices)


def informar_menos_votado(votos_partidos):
    """Opcion 9: partido(s) con la menor cantidad de votos

    Args:
        votos_partidos (list): Votos de cada partido

    Returns:
        int: Cantidad de partidos con el minimo de votos
    """
    salidas.mostrar_titulo("Partido menos votado")
    indices = funciones.buscar_indices_menos_votados(votos_partidos)
    listar_partidos(votos_partidos, indices)
    return len(indices)


def informar_segunda_vuelta(votos_partidos):
    """Opcion 10: informa si hay segunda vuelta y, si no, el ganador

    Args:
        votos_partidos (list): Votos de cada partido

    Returns:
        bool: True si hay segunda vuelta, False si no
    """
    salidas.mostrar_titulo("Verificacion de segunda vuelta")
    hay_segunda_vuelta = funciones.verificar_segunda_vuelta(votos_partidos)
    if hay_segunda_vuelta:
        salidas.mostrar_mensaje("Debe realizarse una segunda vuelta electoral")
    else:
        salidas.mostrar_mensaje(
            "No debe realizarse una segunda vuelta electoral"
        )
        maximo = funciones.obtener_maximo(votos_partidos)
        indices = [votos_partidos.index(maximo)]
        salidas.mostrar_mensaje("Partido ganador:")
        listar_partidos(votos_partidos, indices)
    return hay_segunda_vuelta


def procesar_opcion(opcion, votos_partidos):
    """Ejecuta la opcion elegida (2 a 11) sobre los votos cargados

    Args:
        opcion (int): Opcion del menu elegida
        votos_partidos (list): Votos de cada partido

    Returns:
        list: La lista de votos (puede haber sido reemplazada)
    """
    if opcion == 2:
        informar_votos_partidos(votos_partidos)
    elif opcion == 3:
        informar_menores_porcentaje(votos_partidos, 10)
    elif opcion == 4:
        informar_menores_porcentaje(votos_partidos, 15)
    elif opcion == 5:
        informar_menores_porcentaje(votos_partidos, 20)
    elif opcion == 6:
        informar_mayores_votos(votos_partidos, 500)
    elif opcion == 7:
        informar_mayores_votos(votos_partidos, 1000)
    elif opcion == 8:
        informar_sobre_promedio(votos_partidos)
    elif opcion == 9:
        informar_menos_votado(votos_partidos)
    elif opcion == 10:
        informar_segunda_vuelta(votos_partidos)
    elif opcion == 11:
        funciones.reemplazar_votos_hardcodeados(votos_partidos)
        salidas.mostrar_mensaje("Vector reemplazado por datos hardcodeados")
    return votos_partidos


def ejecutar_menu():
    """Ejecuta el menu principal hasta que el usuario elija salir

    Returns:
        list: Lista de votos con la que termino el programa
    """
    votos_partidos = []
    opcion = -1
    while opcion != 0:
        salidas.mostrar_menu()
        opcion = entradas.pedir_opcion_menu(0, 11)
        if opcion == 0:
            salidas.mostrar_mensaje("Programa finalizado")
        elif opcion == 1:
            cargar_votos_partidos(votos_partidos)
        elif not funciones.verificar_votos_cargados(votos_partidos):
            salidas.mostrar_error(
                "Primero debe cargar los votos (opcion 1)"
            )
        else:
            procesar_opcion(opcion, votos_partidos)
    return votos_partidos
