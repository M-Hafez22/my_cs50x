
import webbrowser

class Movie():   #making a class with uper case letter
	'''this class provides a way to store move related information ''' #>>that is the __doc__
	VLID_RATINGS = ["G", "PG" ,"PG-13","R"]   #class variable
	#the firest instance method  ( __init__ )
	def __init__(self, movie_title,movie_storyLine,poster_image,trailer_youtube):
		self.title =movie_title      # instance variable
		self.storyLine = movie_storyLine
		self.poster_image_url = poster_image
		self.trailer_youtube_url =trailer_youtube

	#the second instance method	( show_trailer )
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

	"""docstring for Movie"""
	
        
    