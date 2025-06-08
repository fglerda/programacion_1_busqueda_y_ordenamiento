def ordenar_estudiantes(lista, criterio):
    if criterio == "apellido":
        return sorted(lista, key=lambda x: x["apellido"])
    elif criterio == "promedio":
        return sorted(lista, key=lambda x: x["promedio"], reverse=True)
    elif criterio == "carrera":
        return sorted(lista, key=lambda x: x["carrera"])
    elif criterio == "legajo":
        return sorted(lista, key=lambda x: x["legajo"])
    else:
        raise ValueError("Criterio no válido. Usa 'apellido', 'promedio' o 'carrera'.")


if __name__ == "__main__":
    from lista_estudiantes import generar_estudiante_ficticio

    estudiantes = [generar_estudiante_ficticio(i) for i in range(1, 11)]
    ordenados = ordenar_estudiantes(estudiantes, "apellido")
    for est in ordenados:
        print(est)
