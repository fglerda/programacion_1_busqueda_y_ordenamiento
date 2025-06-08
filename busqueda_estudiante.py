from ordenar_estudiantes import ordenar_estudiantes


def busqueda_binaria_estudiante(lista, criterio, valor_busqueda):
    """
    Realiza una búsqueda binaria sobre la lista de estudiantes ordenada por el criterio dado.
    Retorna el estudiante si lo encuentra, o None si no existe.
    """
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        estudiante = lista[medio]
        valor_actual = estudiante[criterio]

        # Para promedio, convertir a float para comparar correctamente
        if criterio == "promedio":
            valor_actual = float(valor_actual)
            valor_busqueda = float(valor_busqueda)

        if valor_actual == valor_busqueda:
            return estudiante
        elif valor_actual < valor_busqueda:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return None


################################################################
# Ejemplo de uso:
if __name__ == "__main__":
    from lista_estudiantes import generar_estudiante_ficticio

    estudiantes = [generar_estudiante_ficticio(i) for i in range(1, 21)]
    criterio = "apellido"  # Puede ser "apellido", "promedio" o "carrera"
    estudiantes_ordenados = ordenar_estudiantes(estudiantes, criterio)
    valor_a_buscar = estudiantes_ordenados[5][
        criterio
    ]  # Por ejemplo, buscar el 6to apellido

    resultado = busqueda_binaria_estudiante(
        estudiantes_ordenados, criterio, valor_a_buscar
    )
    if resultado:
        print("Estudiante encontrado:", resultado)
    else:
        print("Estudiante no encontrado.")
