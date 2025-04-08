# PR1 - Web Scraping de FilmAffinity

## Autor
- Luciano Hauser Tortosa

---

## Estructura del repositorio

```
/PR1-Lucianohauser13
├── source/
│   └── film_scraper.py          # Código Python para extraer datos desde FilmAffinity
├── dataset/
│   └── filmaffinity_movies.csv  # Dataset generado por el script de scraping
├── requirements.txt             # Archivo con todas las librerías necesarias
├── README.md                    # Este documento
```

---

## Cómo usar el código

### Requisitos

Antes de ejecutar el script, asegúrate de tener Python instalado (versión 3.7 o superior). Puedes instalar las dependencias ejecutando:

```bash
pip install -r requirements.txt
```

### Ejecución

Desde la raíz del proyecto, ejecuta el siguiente comando:

```bash
python source/film_scraper.py
```

Este script realizará scraping sobre el ranking de películas de FilmAffinity y generará un archivo `filmaffinity_movies.csv` en la carpeta `/dataset`.

### Parámetros

El script actual no admite parámetros por línea de comandos; sin embargo, puedes modificar directamente la variable `url` dentro del script para adaptarlo a otras páginas internas de FilmAffinity si se desea ampliar el dataset.

---

## ¿Qué hace el script?

- Accede a la página de ranking de películas en FilmAffinity.
- Extrae para cada película los siguientes datos:
  - Título
  - Año de estreno
  - País de origen
  - Calificación promedio
  - Número de votos
  - Director
  - Reparto principal
  - Enlace a la ficha de la película
- Almacena los datos en un DataFrame de `pandas`.
- Exporta el resultado en un archivo CSV.

---

##  Dataset generado

El dataset se encuentra publicado en Zenodo y accesible públicamente bajo una licencia abierta:

 **DOI del dataset:** [https://zenodo.org/records/15177922](https://zenodo.org/records/15177922)