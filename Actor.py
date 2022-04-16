class Actor:
    def __init__(self,release_date,genre,actor_name, movie_name):
        """Initalize release date, genre, actor_name, movie_name
    Args:
        release_date(int)- release date of movie
        genre(str)- genre of movie
        actor_name(str)- name of actor in movie
        movie_name(str)- name of movie
        """
  
  
    def get_genre(self,movie_name):
        """return the genre of the movie based on the move name from database
   Args:
       movie_name(str)- the name of the movie
   Returns:
       str- genre of movie
    """
        pass

    def release_date(self,movie_name):
        """return the release date of the movie based on the move name from csv file
   Args:
       movie_name(str)- the name of the movie
   Returns:
       int- release date
    """
        pass
    
    def get_movie(self,movie_name):
        """return the name of the movie from the csv file
    Args:
        movie_name(str) - name of the movie
    Returns:
        str - title of the movie
    """
    
    def get_boxoffice(self,profits):
        """returns the revenue of a film after calculating the difference 
            between the making expenses and the box office collections
    Args:
        profits (int): how much profits the film made
    Returns:
        int - profits
    """
        pass
    
    def get_awards(self,awards):
        """returns a list of awards the particular movie or actor
    Args:
        awards (list): returns a list of strings
    Returns:
        list - list of strings of all the awards
    """
        pass
    
    def recommendations(self, actor_name, genre,awards,movie_name):
        """returns a list of recommendations based on the """
        
        
        
        
    
class Trivia:
    
    def parse_args(arglist):
        """Parse command line arguments
        
        """