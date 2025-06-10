import math
import unicodedata  # Se utiliza para normalizar textos con caracteres especiales


def normalizar(texto):
    texto = texto.lower()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    return texto


def busqueda_binaria_estudiante(lista, criterio, valor_busqueda):
    """
    Realiza una búsqueda binaria de estudiantes según el criterio y valor dado.
    Devuelve una lista de coincidencias o None si no hay resultados.
    """
    resultados = []

    if criterio == "apellido":
        valor_busqueda = normalizar(str(valor_busqueda))
    elif criterio == "promedio":
        valor_busqueda = float(valor_busqueda)
    elif criterio == "legajo":
        valor_busqueda = int(valor_busqueda)

    izquierda = 0
    derecha = len(lista) - 1
    medio = None

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        estudiante = lista[medio]
        valor_actual = estudiante[criterio]

        if criterio == "promedio":
            valor_actual = float(valor_actual)
            if math.isclose(valor_actual, valor_busqueda, abs_tol=1e-2):
                break
            elif valor_actual < valor_busqueda:
                izquierda = medio + 1
            else:
                derecha = medio - 1
        elif criterio == "legajo":
            valor_actual = int(valor_actual)
            if valor_actual == valor_busqueda:
                resultados.append(estudiante)
                return resultados
            elif valor_actual < valor_busqueda:
                izquierda = medio + 1
            else:
                derecha = medio - 1
        elif criterio == "apellido":
            valor_actual_norm = normalizar(str(valor_actual))
            if valor_actual_norm == valor_busqueda:
                # Buscar todos los que tengan el mismo apellido (normalizado)
                # Buscar hacia la izquierda
                i = medio
                while i >= 0 and normalizar(str(lista[i][criterio])) == valor_busqueda:
                    resultados.append(lista[i])
                    i -= 1
                # Buscar hacia la derecha
                i = medio + 1
                while (
                    i < len(lista)
                    and normalizar(str(lista[i][criterio])) == valor_busqueda
                ):
                    resultados.append(lista[i])
                    i += 1
                return resultados if resultados else None
            elif valor_actual_norm < valor_busqueda:
                izquierda = medio + 1
            else:
                derecha = medio - 1

    # Si el criterio es promedio y encontramos coincidencia, buscamos todos los que coincidan
    if criterio == "promedio" and medio is not None:
        # Buscar hacia la izquierda
        i = medio
        while i >= 0 and math.isclose(
            float(lista[i][criterio]), valor_busqueda, abs_tol=1e-2
        ):
            resultados.append(lista[i])
            i -= 1
        # Buscar hacia la derecha
        i = medio + 1
        while i < len(lista) and math.isclose(
            float(lista[i][criterio]), valor_busqueda, abs_tol=1e-2
        ):
            resultados.append(lista[i])
            i += 1

    return resultados if resultados else None
