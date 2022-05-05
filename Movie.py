import pandas as pd

file = pd.read_csv("/Users/edwardjames/Downloads/326 Final Project - Sheet1.csv")

class Movie:
    
    def __init__(self, release_year, genre, actor, title):
        """initialize release_year, genre, actor_name, title

        Args:
            release_year (int): year the movie was released
            genre (str): the genre of the movie
            actor_name (str): name of lead actor in movie
            title (str): title of movie
        """
        self.release_year = release_year
        self.genre = genre
        self.actor_name = actor
        self.title = title
        
    def movie_list(self):
        """ movies in database
        
        Returns:
            str: list of moves in database
        """
        for line in file:
            mlist = []
            mlist.append(file['Title'])
        print (mlist)
        
    def get_info(self,title):
        """ get info of the movie including release date, genre, and lead actor name

        Args:
            title (str): the title of the movie
        
        Returns:
            release_year (int): year the movie was released
            genre (str): the genre of the movie
            actor_name (str): name of lead actor in movie
        """
        df = file.query(f"Title == {title}")
        #df = file[file.Title.isin([f"{title}"])]
        #df = file[file.Title.str.contains(f"{title}")]
        df = file.filter([f"{title}"])
        
        for line in df:
            release_year = file.loc[(f"{title}"),"Release Year"]
            genre = file.loc[(f"{title}"),"Genre"]
            actor = file.loc[(f"{title}"),"Lead Actor"]
        print(f"the {genre} film {title} was released in {release_year} with lead actor{actor}")
        
class Recomendation:
    
    def __init__(self,genre):
        """Initalize movie recomendation for user

        Args:
            genre (str): genre of movies
        """
    
    
    def user_choice(self):
        """Store input of users favorite genre of movie
        """
        
    def recommend_movie(self, genre):
        """recomend movie to user based on movie genre

        Args:
            genre (str): genre of movies
            
        Returns:
            string of reccomended movies 
        """
    
    def parse_args(arglist):
        """Parse command line arguments
        
    Args:
        arglist (list of strings): arguments in the command line
    Returns:
        the list of strings in the terminal
    Side effects:
        prints objects to the terminal
     """
        pass
    
    if __name__ == "__main__":
        pass
    