# Algoritmos de Búsqueda y Ordenamiento en Python

## Descripción General

Este proyecto implementa un sistema en Python para ordenar y buscar registros de estudiantes a partir de datos almacenados en un archivo CSV. Los algoritmos utilizados permiten ordenar por diferentes criterios (apellido, promedio, legajo, carrera) y realizar búsquedas eficientes utilizando el método de búsqueda binaria.

## Estructura del Proyecto

- programa_unificado.py: Script principal que coordina la carga de datos, ordenamiento, búsqueda y visualización de resultados. Es el archivo a ejecutar.
- ordenar_estudiantes.py: Contiene funciones para ordenar listas de estudiantes por distintos criterios usando sorted().
- busqueda_estudiante.py: Implementa la búsqueda binaria, adaptada a diferentes tipos de datos.
- estudiantes.csv: Archivo de entrada con los datos de estudiantes (no incluido aquí).
- README.md: Este archivo de documentación.

## Funcionalidades

- Carga de datos desde un archivo CSV.
- Ordenamiento por:
  - Apellido (con normalización para evitar problemas con tildes)
  - Promedio
  - Legajo
  - Carrera
- Búsqueda binaria según el criterio seleccionado.
- Medición del tiempo de ejecución de la búsqueda.
- Impresión de resultados en consola.

## Requisitos

- Python 3.7 o superior

## Ejecución

1. Colocar el archivo `estudiantes.csv` en el mismo directorio.
2. Ejecutar el archivo principal:
   ```bash
   python programa_unificado.py
   ```
3. Ingresar el criterio de ordenamiento/búsqueda (legajo, apellido o promedio).
4. Ingresar el valor de búsqueda cuando se solicite.

## Ejemplo de uso

```
Ingrese el criterio de orden/búsqueda: apellido

Estudiantes ordenados por apellido:
...
Ingrese el valor a buscar por apellido: Garcia

Estudiantes encontrados:
{'legajo': 123, 'apellido': 'García', 'nombre': 'Lucía', 'promedio': 8.5}
```

## Link video explicativo


## Créditos

Trabajo realizado para la materia *Programación I* – Tecnicatura Universitaria en Programación (a distancia) UTN.

Autores:  Lerda Fernando – fglerda@gmail.com
          Lopez Joana – Jl105658@gmail.com 

## Licencia

Este proyecto es de uso académico y educativo.