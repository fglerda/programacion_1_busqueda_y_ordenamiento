import unicodedata  # Se utiliza para normalizar textos con caracteres especiales


def normalizar(texto):
    texto = texto.lower()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    return texto


def ordenar_estudiantes(lista, criterio):
    if criterio == "apellido":
        return sorted(lista, key=lambda x: normalizar(x["apellido"]))
    elif criterio == "promedio":
        return sorted(
            lista,
            key=lambda x: x["promedio"],
        )
    elif criterio == "carrera":
        return sorted(lista, key=lambda x: x["carrera"])
    elif criterio == "legajo":
        return sorted(lista, key=lambda x: x["legajo"])
    else:
        raise ValueError("Criterio no válido. Usa 'apellido', 'promedio' o 'carrera'.")
