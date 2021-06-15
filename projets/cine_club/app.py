# Créer l'interface graphique
from PySide2 import QtWidgets, QtCore
from movie import get_movies
from movie import Movie

class App(QtWidgets.QWidget):
    def __init__(self):
       super().__init__()
       self.setWindowTitle("Ciné club")
       self.setup_ui()
       self.populate_movies()
       self.setup_connections()

        # Ajouter un film
    def setup_ui(self):
        self.main_layout = QtWidgets.QVBoxLayout(self)

        self.le_movieTitle = QtWidgets.QLineEdit()
        self.btn_addMovie = QtWidgets.QPushButton("Ajouter un film")
        self.lw_movies = QtWidgets.QListWidget()
        self.lw_movies.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        self.btn_removeMovies = QtWidgets.QPushButton("Supprimer le(s) film(s)")
      
        self.main_layout.addWidget(self.le_movieTitle)
        self.main_layout.addWidget(self.btn_addMovie)
        self.main_layout.addWidget(self.lw_movies)
        self.main_layout.addWidget(self.btn_removeMovies)
        
        # Connecter les widgets aux méthodes
    def setup_connections(self):
        self.btn_addMovie.clicked.connect(self.add_movie)
        self.btn_removeMovies.clicked.connect(self.remove_movie)
        self.le_movieTitle.returnPressed.connect(self.add_movie)
        # Connecter les widgets aux méthodes End.

        # Ajouter les films dans la liste
    def populate_movies(self):
        movies = get_movies()

        for movie in movies:
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.movie = movie
            # lw_item.setData(QtCore.Qt.UserRole , movie)
            self.lw_movies.addItem(lw_item)     
        # Ajouter les films dans la liste End.
        
        # Connecter les widgets aux méthodes
    
    def add_movie(self):
        # Recupérer le texte dans le line edit
        movie_title = self.le_movieTitle.text()
        if not movie_title:
            return False
        # Recupérer le texte dans le line edit End.

        # Créer une instance 'Movie'
        movie = Movie(title=movie_title)
        resultat = movie.add_to_movies()
        # Créer une instance 'Movie' End.
        
        # Ajouter le film dans le fichier json
        if resultat:
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.movie = movie
            # lw_item.setData(QtCore.Qt.UserRole , movie)
            self.lw_movies.addItem(lw_item)
        # Ajouter le film dans le fichier json End.
        
        # Ajouter le titre du film dans la list widget
        self.le_movieTitle.setText("")
        # Ajouter le titre du film dans la list widget End

        # On supprime un film
    def remove_movie(self):
        for selected_item in self.lw_movies.selectedItems():
            movie = selected_item.movie
            #movie = selected_item.data(QtCore.Qt.UserRole)
            movie.remove_from_movies()
            self.lw_movies.takeItem(self.lw_movies.row(selected_item))
        # Connecter les widgets aux méthodes End

app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()
# Créer l'interface graphique End.