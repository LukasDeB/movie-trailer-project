import webbrowser   

class Movie() :
    def __init__(self, movie_title, movie_storyline, movie_trailer, image_url) :
        self.title = movie_title
        self.storyline = movie_storyline
        self.trailer_youtube_url = movie_trailer
        self.poster_image_url = image_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
