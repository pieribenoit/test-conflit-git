import os
import json
import logging

CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, "data", "movies.json")
       
       
  # Céer une fonction pour recupérer tous les films
def get_movies():
    with open(DATA_FILE, "r") as f:
        movies_title = json.load(f)

    movies = [Movie(movie_title) for movie_title in movies_title]
    return movies

class Movie:
    def __init__(self, title):
        self.title = title.title()

    def __str__(self):
        return self.title
      # Céer des methodes 'get' et 'write'
    def _get_movies(self):
      with open(DATA_FILE, "r") as f:
            return json.load(f)

    def _write_movies(self, movies):
       with open(DATA_FILE, "w") as f:
            json.dump(movies, f, indent=4)      
       # Céer des methodes 'get' et 'write' End
       
       # Céer une methodes pour ajouter un film
    def add_to_movies(self):
        # Récupérer la liste des films
        movies = self._get_movies()
        # Vérifier que le film n'est pas déjà dans la liste
        # Si ce n'est pas le cas on l'ajoute
        if self.title not in movies:
            movies.append(self.title)
            self._write_movies(movies)
            return True
        # Si c'est le cas, on affiche un message pour indiquer
        # Que le film est déjà dans la liste (avec le module
        # Logging).
        else:
            logging.warning(f"Le film {self.title} est déjà enregistré.")
            return False
       # Céer une methodes pour ajouter un film End.


    def remove_from_movies(self):
        # Récupérer la liste des films
        movies = self._get_movies()
        # Vérifier que le film est dans la liste
        if self.title in movies:
            movies.remove(self.title)
            self._write_movies(movies)
        # Si c'est le cas, enlever le film de la liste 
        # et écrire la nouvelle liste de films dans le fichier
        # json.
       # Céer une methodes pour ajouter un film End.



if __name__ == "__main__":
   movies = get_movies()
   print(movies)