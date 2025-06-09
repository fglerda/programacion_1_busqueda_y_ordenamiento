import csv
import timeit
from ordenar_estudiantes import ordenar_estudiantes
from busqueda_estudiante import busqueda_binaria_estudiante


def cargar_estudiantes_csv(ruta):
    estudiantes = []
    with open(ruta, encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            # Convertir promedio a float para búsquedas numéricas
            fila["promedio"] = float(fila["promedio"])
            # Convertir legajo a int para búsquedas numéricas
            fila["legajo"] = int(fila["legajo"])
            estudiantes.append(fila)
    return estudiantes


def main():
    ruta = "estudiantes.csv"
    estudiantes = cargar_estudiantes_csv(ruta)

    print("Criterios disponibles: legajo, apellido, promedio")
    criterio = input("Ingrese el criterio de orden/búsqueda: ").strip().lower()
    if criterio not in ["legajo", "apellido", "promedio"]:
        print("Criterio no válido.")
        return

    estudiantes_ordenados = ordenar_estudiantes(estudiantes, criterio)
    print("\nEstudiantes ordenados por", criterio)
    for est in estudiantes_ordenados[:501]:
        print(
            f"{est['legajo']} - {est['apellido']} - {est['nombre']} - {est['promedio']}"
        )

    valor = input(f"\nIngrese el valor a buscar por {criterio}: ").strip()
    # Convertir valor de búsqueda si es necesario
    if criterio == "legajo":
        valor = int(valor)
    elif criterio == "promedio":
        valor = float(valor)
    # Medir tiempo de búsqueda para la busqueda binaria
    start_time = timeit.default_timer()
    resultado = busqueda_binaria_estudiante(estudiantes_ordenados, criterio, valor)
    end_time = timeit.default_timer()
    if resultado:
        print("\nEstudiantes encontrados:")
        for est in resultado:
            print(est)  # Esto imprime todo el diccionario del estudiante
    else:
        print("\nEstudiante no encontrado.")
    print(f"\nTiempo de búsqueda binaria: {end_time - start_time:.6f} segundos")


if __name__ == "__main__":
    main()
