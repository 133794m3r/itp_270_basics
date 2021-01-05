"""
Movie Class models a movie in the theater.
Properties
name: a string.
rating: one of [G, PG, PG-13, R]
cost to see: Some floating point value.
desc: A string describing the movie.
The last method is optional and should default to an empty string.

Methods
Should just have an init method, and maybe a way to print it's properties.
"""

"""
MovieTheater Class holds all of the movies.

Properties
movies is a dict that contains a collection of Movie objects.
Example of a single movie is something like 
['movie':Movie('test','G',10.00),'tickets':0]

methods
add_movie
this method should let the person add a movie to be shown. it should set the tickets value to 0. if the movie already exists return false, and print the error "Movie already exists".
It should only take a Movie object as it's only parameter.


purchase_ticket
This method should take a parameter of the movie name. If the movie exists it should increment the number of movies sold by 1.


print_sales
This method should print all of the movies, and how many tickets were sold.
Finally it should print "The theater made $XX today". Where XX is the amount of money it made.

This value is simply calculated by multiplying the number of tickets sold for each movie by the cost of that movie. Then adding that to the total. Finally that value is our total.


OPTIONAL METHODS
movie_info
This method should return the following information in a string.

movie_name Rating:movie_rating Cost:movie_cost\n(new line)
movie_description


list_movies
This method should return the title and rating of each movie that we currently have.
"""

"""
You have skeletons of the classes given to you below. You have to modify the init functions to take the parameters as described above.

Further the methods need to be filled out as described above.
"""

class Movie:
	name = ""
	cost = 0.0
	rating = ""
	desc = ""
	def __init__(self):
		pass


class MovieTheater:
	movies = []

	def __init__(self):
		pass

	def add_movie(self,movie):
		pass

	def purchase_ticket(self,movie_title):
		pass

	def list_movies(self):
		pass

	def movie_info(self):
		pass

	def print_sales(self):
		pass