# Importación de librerías necesarias
import requests  # Para hacer peticiones HTTP al sitio web
from bs4 import BeautifulSoup  # Para parsear y navegar el contenido HTML
import pandas as pd  # Para almacenar y manipular los datos en forma de DataFrame
import re  # Para limpiar los datos de votos con expresiones regulares

# Definición de la función principal que realiza el scraping
def scrape_filmaffinity_from_web(url):
    # Realiza la petición HTTP al sitio web
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error al acceder a la página: {response.status_code}")
        return None

    # Parsear el contenido HTML con BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    movies = []  # Lista vacía donde se almacenarán los diccionarios con los datos de cada película

    # Seleccionar todos los bloques de películas (cada elemento <li> dentro del ranking)
    movie_blocks = soup.select('.fa-list-group li')

    # Iterar sobre cada bloque de película y extraer los datos necesarios
    for item in movie_blocks:
        # Extraer título de la película
        try:
            title = item.select_one('.mc-title a').text.strip()
        except AttributeError:
            title = None

        # Extraer el enlace completo a la página de la película
        try:
            link = 'https://www.filmaffinity.com' + item.select_one('.mc-title a')['href']
        except (AttributeError, TypeError):
            link = None

        # Extraer el país de origen (se obtiene del atributo alt de la bandera)
        try:
            country = item.select_one('.nflag')['alt']
        except (AttributeError, TypeError):
            country = None

        # Extraer el año de estreno
        try:
            year = item.select_one('.mc-year').text.strip()
        except AttributeError:
            year = None

        # Extraer la calificación promedio, reemplazando coma por punto para formato numérico
        try:
            rating_element = item.select_one('.fa-avg-rat-box .avg')
            rating = rating_element.text.strip().replace(',', '.') if rating_element else None
        except AttributeError:
            rating = None

        # Extraer el número de votos, eliminando caracteres no numéricos (como puntos)
        try:
            votes_element = item.select_one('.fa-avg-rat-box .count')
            if votes_element:
                votes = re.sub(r'[^\d]', '', votes_element.text.strip())  # solo deja números
            else:
                votes = None
        except AttributeError:
            votes = None

        # Extraer el nombre del director
        try:
            director = item.select_one('.mc-director .nb a').text.strip()
        except AttributeError:
            director = None

        # Extraer la lista de actores principales y convertirla en una cadena separada por comas
        try:
            actors = [actor.text.strip() for actor in item.select('.mc-cast .nb a')]
            actors = ', '.join(actors)
        except AttributeError:
            actors = None

        # Crear un diccionario con todos los datos recolectados
        movie = {
            'Title': title,
            'Year': year,
            'Country': country,
            'Rating': rating,
            'Votes': votes,
            'Director': director,
            'Actors': actors,
            'Link': link
        }

        # Agregar el diccionario a la lista de películas
        movies.append(movie)

    # Convertir la lista de películas en un DataFrame de pandas
    movies_df = pd.DataFrame(movies)

    # Guardar el DataFrame en un archivo CSV codificado en UTF-8
    movies_df.to_csv('dataset/filmaffinity_movies.csv', index=False, encoding='utf-8-sig')
    print("Archivo CSV guardado como 'filmaffinity_movies.csv'")

    return movies_df

# URL de la página de FilmAffinity que contiene el ranking
url = "https://www.filmaffinity.com/es/ranking.php?rn=ranking_fa_movies"

# Llamada a la función para ejecutar el scraping
scrape_filmaffinity_from_web(url)
