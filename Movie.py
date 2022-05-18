import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from argparse import ArgumentParser
import sys




file = pd.read_csv("movie_data.csv")

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
        
        for line in file:
            release_year = file.loc[file.Title == title, 'Release Year'].tolist()
            genre = file.loc[file.Title == title, 'Genre'].tolist()
            actor = file.loc[file.Title == title, 'Lead Actor'].tolist()
            print(f"The {genre} film {title} was released in {release_year} with lead actor{actor}")
            break
        
              
class Recomendation:
    
    def __init__(self,genre):
        """Initalize movie recomendation for user

        Args:
            genre (str): genre of movies
        """
        self.genre = genre
    
    def user_choice(self):
        """Store input of users favorite genre of movie
        """
        fav_genre = input("Enter your favorite movie genre: ")
        
    def recommend_movie(self, genre):
        """recomend movie to user based on movie genre

        Args:
            genre (str): genre of movies
            
        Returns:
            string of recomended movies 
        """
        if self.user_choice == "Superhero":
            genre_filter = file["Genre"] == "Superhero"
            superhero_df = file[genre_filter]
            cols = ["Title","Genre"]
            final = superhero_df[cols]
            

        elif self.user_choice == "Action/Adventure":
            genre_filter = file["Genre"] == "Action/Adventure"
            action_df = file[genre_filter]
            cols = ["Title", "Genre"]
            final = action_df[cols]
        
        elif self.user_choice == "Romance/Drama":
            genre_filter = file["Genre"] == "Romance/Drama"
            romance_df = file[genre_filter]
            cols = ["Title", "Genre"]
            final = romance_df[cols]
        
        elif self.user_choice == "Family/Adventure":
            genre_filter = file["Genre"] == "Family/Adventure"
            family_df = file[genre_filter]
            cols = ["Title", "Genre"]
            final = family_df[cols]
        
        elif self.user_choice == "Animation":
            genre_filter = file["Genre"] == "Animation"
            animation_df = file[genre_filter]
            cols = ["Title", "Genre"]
            final = animation_df[cols]
            
        print(final)
        
def actor(self, actor):
        more_info = input("Would you like to learn more about any of these movies? (y/n): ")
        if more_info.lower == "n" or "no":
            return

        if more_info.lower == "y" or "yes":
            movie_info = input("Movie name: ")
            print(f"The lead actor for this movie is {movie_info.actor}")

def box_office(self):
    df = pd.read_csv("movie_data.csv")
    print(df['Title', 'Box Office'])
    print(sns.lmplot(x = 'Genre', y = 'Box Office', data = df))   
            
        
            
        

def parse_args(arglist):
    """Parse command line arguments
        
Args:
    arglist (list of strings): arguments in the command line
Returns:
    the list of strings in the terminal
Side effects:
    prints objects to the terminal
    """
    
    parser = ArgumentParser()
    parser.add_argument("file")
    return parser.parse_args(arglist)

    
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    Recomendation(args.file)


    
