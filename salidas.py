def mostrar_menu():
    print("\n===== SISTEMA DE GESTION DE ELECCIONES - UTN FRA =====")
    print("1.  Cargar votos")
    print("2.  Mostrar votos")
    print("3.  Partidos con menos del 10% de votos")
    print("4.  Partidos con menos del 15% de votos")
    print("5.  Partidos con menos del 20% de votos")
    print("6.  Partidos con más de 500 votos")
    print("7.  Partidos con más de 1000 votos")
    print("8.  Partidos por encima del promedio")
    print("9.  Partido menos votado")
    print("10. Verificar segunda vuelta")
    print("11. Hardcodear vector")
    print("0.  Salir")


def mostrar_mensaje(mensaje):
    """Muestra un mensaje informativo

    Args:
        mensaje (str): Texto a mostrar
    """
    print(mensaje)


def mostrar_error(mensaje):
    """Muestra un mensaje de error

    Args:
        mensaje (str): Texto del error
    """
    print(f"ERROR: {mensaje}")


def mostrar_titulo(titulo):
    """Muestra un titulo de seccion con separadores

    Args:
        titulo (str): Titulo a mostrar
    """
    print("\n" + "-" * 50)
    print(titulo)
    print("-" * 50)


def mostrar_partido(indice, cantidad_votos, porcentaje):
    """Muestra los datos de un partido politico

    Args:
        indice (int): Posicion del partido en el vector (desde 0)
        cantidad_votos (int): Votos recibidos por el partido
        porcentaje (float): Porcentaje de votos del partido
    """
    print(f"Partido {indice + 1}: {cantidad_votos} votos ({porcentaje:.2f}%)")


def mostrar_resumen_general(cantidad_partidos, total_votos):
    """Muestra la cantidad de partidos postulados y el total de votos

    Args:
        cantidad_partidos (int): Cantidad de partidos postulados
        total_votos (int): Cantidad total de votos
    """
    print(f"\nPartidos postulados: {cantidad_partidos}")
    print(f"Total de votos: {total_votos}")


def mostrar_porcentaje_acumulado(porcentaje):
    """Muestra el porcentaje acumulado de un conjunto de resultados

    Args:
        porcentaje (float): Porcentaje acumulado
    """
    print(f"\nPorcentaje de votos acumulado: {porcentaje:.2f}%")


def mostrar_promedio_general(promedio):
    """Muestra el promedio general de votos 

    Args:
        promedio (float): Promedio de votos de todos los partidos
    """
    print(f"Promedio general de votos: {promedio:.2f}")


def mostrar_resumen_busqueda(suma_votos, cantidad_partidos, promedio):
    """Muestra suma, cantidad y promedio de una busqueda

    Args:
        suma_votos (int): Suma de votos de los resultados
        cantidad_partidos (int): Cantidad de partidos encontrados
        promedio (float): Promedio de votos de los resultados
    """
    print(f"\nSuma de votos: {suma_votos}")
    print(f"Cantidad de partidos: {cantidad_partidos}")
    print(f"Promedio de votos: {promedio:.2f}")
