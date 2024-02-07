from bs4 import BeautifulSoup
import requests
import time


def get_movies(cinema_page: str) -> list[str]:
    """ Processes 
    """
    response = requests.get(cinema_page)
    soup = BeautifulSoup(response.text, 'html.parser')

    movies = []
    items = soup.find_all('article', class_='movie-compare')
    for each in items:
        divs = each.find_all('div')
        name = divs[0].find('h2').text
        movies.append(name)

    return movies

movies = get_movies('https://uae.voxcinemas.com/showtimes?c=mall-of-the-emirates')
for each in movies:
    print(each)

# TODO: 
# See what happens when we change that url to a different vox cinema!
# See what happens when we time that request, and talk about the journey of a request


