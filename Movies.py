import pandas as pd

class Movie:
    
    def __init__(self, release_year, genre, actor_name, title):
        """initialize release_year, genre, actor_name, title

        Args:
            release_year (int): year the movie was released
            genre (str): the genre of the movie
            actor_name (str): name of lead actor in movie
            title (str): title of movie
        """
        self.release_year = release_year
        self.genre = genre
        self.actor_name = actor_name
        self.title = title
        
    def get_info(self,title):
        """ get info of the movie including release date, genre, and lead actor name

        Args:
            title (str): the title of the movie
        
        Returns:
            release_year (int): year the movie was released
            genre (str): the genre of the movie
            actor_name (str): name of lead actor in movie
        """
    def movie_list(self):
        """ movies in database
        
        Returns:
            str: list of moves in database
        """
class Recomendation:
    
    def __init__(self,genre):
        """Initalize movie recomendation for user

        Args:
            genre (str): genre of movies
        """
    
    def recommend_movie(self, genre):
        """recomend movie to user based on movie genre

        Args:
            genre (str): genre of movies
        """
    def user_choice(self):
        """Store input of users favorite genre of movie
        """