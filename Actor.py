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

    def release_date(self,movie_name):
        """return the release date of the movie based on the move name from csv file
   Args:
       movie_name(str)- the name of the movie
   Returns:
       int- release date
    """
    
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
    
    def get_awards(self,awards):
        """returns a list of awards the particular movie or actor
    Args:
        awards (list): returns a list of strings
    Returns:
        list - list of strings of all the awards
    """
    
    def recommendations(self, actor_name, genre,awards,movie_name):
        """returns a list of recommendations based on the """
        
        
        
        
    
class Trivia:
    
    def __innit__(self,question,answer,response):
        """Initialize question and answer and response parameters

        Args:
            question (str): trivia question that is being asked
            answer (str): answer to trivia question
            response(str): users response to trivia question
        """
    def ask_question(self,question):
        """ask user a question based on movie/actor

        Args:
            question (str): question based on movie/actor
            
        Return: (str):question that user must answer

        """
    def user_response(self, response):
        """store users response to question

        Args:
            response (str): user response to trivia question
            
        Returns: user response to trivia question
        """
    
    def validate_response(self, response, answer):
        """validate that users response to question is correct

        Args:
            response (str): user response
            answer (str): answer to question
        Returns:
            Bool - True or False
        """
    def win(self,strikes):
        """return statment that user has won the game if they get less than 3 wrong
        Args:
            strike (int): the amont of times user has entered a wrong answer
        Returns:
            Print statement telling user they won the game
        """
    
    def lose(self,strikes):
        """return statment that user has lost the game if they get more than 3 wrong
        Args:
            strike (int): the amont of times user has entered a wrong answer
            
        Returns:
            Print statement telling user they lost the game
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
    