def limpiar_lista(lista):
    """Vacia una lista eliminando todos sus elementos

    Args:
        lista (list): Lista a limpiar

    Returns:
        list: La misma lista, ya vacia
    """
    while len(lista) > 0:
        lista.pop()
    return lista


def reemplazar_votos_hardcodeados(votos_partidos):
    """Reemplaza el contenido de la lista por los votos hardcodeados

    Args:
        votos_partidos (list): Lista que se sobreescribe

    Returns:
        list: La misma lista con los datos hardcodeados
    """
    limpiar_lista(votos_partidos)
    datos = [888, 555, 60, 1850, 999, 777, 1400, 180, 2500, 60]
    for i in range(len(datos)):
        votos_partidos.append(datos[i])
    return votos_partidos


def verificar_votos_cargados(votos_partidos):
    """Verifica si ya se cargaron votos

    Args:
        votos_partidos (list): Lista de votos

    Returns:
        bool: True si la lista tiene datos, False si esta vacia
    """
    return len(votos_partidos) > 0


def calcular_suma(lista):
    """Calcula la suma de los elementos de una lista

    Args:
        lista (list): Lista de numeros

    Returns:
        int: Suma de todos los elementos
    """
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    return suma


def calcular_porcentaje(parte, total):
    """Calcula que porcentaje representa una parte sobre el total

    Args:
        parte (int): Valor parcial
        total (int): Valor total

    Returns:
        float: Porcentaje (0.0 si el total es cero)
    """
    porcentaje = 0.0
    if total > 0:
        porcentaje = parte * 100 / total
    return porcentaje


def calcular_promedio(suma, cantidad):
    """Calcula un promedio evitando la division por cero

    Args:
        suma (int): Suma de los valores
        cantidad (int): Cantidad de valores

    Returns:
        float: Promedio (0.0 si la cantidad es cero)
    """
    promedio = 0.0
    if cantidad > 0:
        promedio = suma / cantidad
    return promedio


def obtener_maximo(lista):
    """Obtiene el mayor valor de una lista

    Args:
        lista (list): Lista de numeros no negativos

    Returns:
        int: Mayor valor (0 si la lista esta vacia)
    """
    maximo = 0
    if len(lista) > 0:
        maximo = lista[0]
        for i in range(len(lista)):
            if lista[i] > maximo:
                maximo = lista[i]
    return maximo


def obtener_minimo(lista):
    """Obtiene el menor valor de una lista

    Args:
        lista (list): Lista de numeros

    Returns:
        int: Menor valor (0 si la lista esta vacia)
    """
    minimo = 0
    if len(lista) > 0:
        minimo = lista[0]
        for i in range(len(lista)):
            if lista[i] < minimo:
                minimo = lista[i]
    return minimo


def buscar_indices_menores_porcentaje(votos_partidos, limite):
    """Busca los partidos con menos de un porcentaje de votos

    Compara con enteros (votos * 100 < limite * total) para evitar
    errores de redondeo

    Args:
        votos_partidos (list): Votos de cada partido
        limite (int): Porcentaje limite (exclusivo)

    Returns:
        list: indices de los partidos que cumplen la condicion
    """
    total = calcular_suma(votos_partidos)
    indices = []
    for i in range(len(votos_partidos)):
        if votos_partidos[i] * 100 < limite * total:
            indices.append(i)
    return indices


def buscar_indices_mayores_votos(votos_partidos, limite):
    """Busca los partidos con mas votos que un limite

    Args:
        votos_partidos (list): Votos de cada partido
        limite (int): Cantidad de votos limite (exclusiva)

    Returns:
        list: indices de los partidos que superan el limite
    """
    indices = []
    for i in range(len(votos_partidos)):
        if votos_partidos[i] > limite:
            indices.append(i)
    return indices


def buscar_indices_sobre_promedio(votos_partidos):
    """Busca los partidos que superan el promedio general de votos

    Args:
        votos_partidos (list): Votos de cada partido

    Returns:
        list: indices de los partidos por encima del promedio
    """
    total = calcular_suma(votos_partidos)
    cantidad = len(votos_partidos)
    indices = []
    for i in range(cantidad):
        if votos_partidos[i] * cantidad > total:
            indices.append(i)
    return indices


def buscar_indices_menos_votados(votos_partidos):
    """Busca los partidos con la menor cantidad de votos (admite empates)

    Args:
        votos_partidos (list): Votos de cada partido

    Returns:
        list: indices de los partidos con el minimo de votos
    """
    minimo = obtener_minimo(votos_partidos)
    indices = []
    for i in range(len(votos_partidos)):
        if votos_partidos[i] == minimo:
            indices.append(i)
    return indices


def calcular_votos_por_indices(votos_partidos, indices):
    """Suma los votos de los partidos indicados

    Args:
        votos_partidos (list): Votos de cada partido
        indices (list): indices de los partidos a sumar

    Returns:
        int: Suma de votos de esos partidos
    """
    suma = 0
    for i in range(len(indices)):
        suma += votos_partidos[indices[i]]
    return suma


def calcular_porcentaje_acumulado(votos_partidos, indices):
    """Calcula el porcentaje acumulado de un grupo de partidos

    Args:
        votos_partidos (list): Votos de cada partido
        indices (list): indices de los partidos del grupo

    Returns:
        float: Porcentaje que el grupo representa del total
    """
    suma_grupo = calcular_votos_por_indices(votos_partidos, indices)
    total = calcular_suma(votos_partidos)
    return calcular_porcentaje(suma_grupo, total)


def verificar_segunda_vuelta(votos_partidos):
    """Verifica si corresponde una segunda vuelta electoral

    Hay segunda vuelta si ningun partido supera el 50% (exactamente
    50% tambien la requiere)

    Args:
        votos_partidos (list): Votos de cada partido

    Returns:
        bool: True si debe haber segunda vuelta, False si no
    """
    maximo = obtener_maximo(votos_partidos)
    total = calcular_suma(votos_partidos)
    return maximo * 100 <= total * 50
