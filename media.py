import webbrowser


class Movie():
    """Stores information about a movies

    Takes the title, a poster image url and a youtube trailer
    url for a movie and stores them in public attributes.

    Attributes:
        title: A sting representing the movie title.
        poster_image_url: A string containing the url to the move poster image.
        trailer_youtube_url: A string containing the url to the trailer on
            youtube.
    """

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """Inits Movie with title, poster_image_url and
        trailer_youtube_url
        """
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
