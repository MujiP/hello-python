from bs4 import BeautifulSoup
import requests
import time


def get_movies(cinema_page):
    """ Returns the movies showing on the specified cinema page
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
print(movies)


# TODO: Let's look at this function. Now we don't need to know how it works. We only need to know what it does, and how we can use it.
# What are we passing in, and what are we getting back?
# TODO: How can we use this to get the movies showing at the vox in nakheel mall?
# TODO: Let's collect the urls for the cinemas you usually go to, and put them in variables.
# TODO: Now let's create a list of those urls, and use a loop to get the movies showing at each cinema.

# TODO: Now what if we want to print the name of the cinema and then its movies, let's use a dictionary to store the cinema name and urls.
# TODO: Now we'll loop over the dictionary. But let's test what looping over a dictionary looks like in a playground.

# TODO: Let's learn how to time the function, see how long each call takes.
# TODO: Let's talk about the journey of a request, from computer to router to network room to ISP to Vox's servers and back again.
# We can even take a look at the network room and see the DU / Etisalat modem.
# It's like Ralph breaks the internet, we're sending a message in a little capsule, and it's going on a journey and coming back with something

# TODO: Let's talk about functions, and how they're like recipes. They take ingredients, they do something with those ingredients, and give back something.
# TODO: Defining a function is like writing a recipe. Calling the function is like performing the recipe. Here's the recipe for chicken curry, and now we make chicken curry.
# TODO: See what happens if we comment out the function definition and call the function anyway.
# TODO: Let's talk about lists.


# FUTURE: We can use this to learn about sets and set operations, and how we can use them to compare the movies showing at different cinemas.
# FUTURE: We can write the movies to a file so save time when we want to re-run the program with changes.
# FUTURE: We can make a program that takes in the cinema name (and later a number) and just see the movies showing at that cinema, instead of having it run all the cinemas every time.

# See what happens when we change that url to a different vox cinema!
# See what happens when we time that request, and talk about the journey of a request

