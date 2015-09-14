from basicmovie import Movie
import basicmovie

class ForrestGump(Movie):
    def __init__(self, movie_title, movie_story, movie_poster, movie_producer):
                Movie.__init__(self, movie_title, movie_story, movie_poster)
                self.movie_producer = movie_producer
    
class Inception(Movie):
    def __init__(self, movie_title, movie_story, movie_poster, movie_trailer, movie_producer):
                Movie.__init__(self, movie_title, movie_story, movie_poster, movie_trailer)
                self.movie_producer = movie_producer

class OneFlewOvertheCuckoosNest(Movie):
    def __init__(self, movie_title, movie_story, movie_poster, movie_trailer, movie_producer):
                Movie.__init__(self, movie_title, movie_story, movie_poster, movie_trailer)
                self.movie_producer = movie_producer

class Shichininnosamurai(Movie):
    def __init__(self, movie_title, movie_story, movie_poster, movie_trailer, movie_producer):
                Movie.__init__(self, movie_title, movie_story, movie_poster, movie_trailer)
                self.movie_producer = movie_producer

class Avatar(Movie):
    def __init__(self, movie_title, movie_story, movie_poster, movie_trailer, movie_producer):
                Movie.__init__(self, movie_title, movie_story, movie_poster, movie_trailer)
                self.movie_producer = movie_producer

class ShawshankRedemption(Movie):
    def __init__(self, movie_title, movie_story, movie_poster, trailer_youtube_url, movie_producer):
                Movie.__init__(self, movie_title, movie_story, movie_poster, trailer_youtube_url)
                self.movie_producer = movie_producer

    def show_trailer(self):
        webbrowser.open(self.movie_trailer_youtube)


class Godfather(Movie):
    def __init__(self, movie_title, movie_story, movie_poster, movie_trailer, movie_producer):
                Movie.__init__(self, movie_title, movie_story, movie_poster, movie_trailer)
                self.movie_producer = movie_producer


class DarkKnight(Movie):
    def __init__(self, movie_title, movie_story, movie_poster, movie_trailer, movie_producer):
                Movie.__init__(self, movie_title, movie_story, movie_poster, movie_trailer)
                self.movie_producer = movie_producer


class SchindlersList(Movie):
    def __init__(self, movie_title, movie_story, movie_poster, movie_trailer, movie_producer):
                Movie.__init__(self, movie_title, movie_story, movie_poster, movie_trailer)
                self.movie_producer = movie_producer

class PulpFiction(Movie):
    def __init__(self, movie_title, movie_story, movie_poster, movie_trailer, movie_producer):
                Movie.__init__(self, movie_title, movie_story, movie_poster, movie_trailer)
                self.movie_producer = movie_producer

class Ilbuonoilbruttoilcattivo(Movie):
    def __init__(self, movie_title, movie_story, movie_poster, movie_trailer, movie_producer):
                Movie.__init__(self, movie_title, movie_story, movie_poster, movie_trailer)
                self.movie_producer = movie_producer

class ReturnoftheKing(Movie):
    def __init__(self, movie_title, movie_story, movie_poster, movie_trailer, movie_producer):
                Movie.__init__(self, movie_title, movie_story, movie_poster, movie_trailer)
                self.movie_producer = movie_producer

class FightClub(Movie):
    def __init__(self, movie_title, movie_story, movie_poster, movie_trailer, movie_producer):
                Movie.__init__(self, movie_title, movie_story, movie_poster, movie_trailer)
                self.movie_producer = movie_producer

class FellowshipoftheRing(Movie):
    def __init__(self, movie_title, movie_story, movie_poster, movie_trailer, movie_producer):
                Movie.__init__(self, movie_title, movie_story, movie_poster, movie_trailer)
                self.movie_producer = movie_producer

class EmpireStrikesBack(Movie):
    def __init__(self, movie_title, movie_story, movie_poster, movie_trailer, movie_producer):
                Movie.__init__(self, movie_title, movie_story, movie_poster, movie_trailer)
                self.movie_producer = movie_producer
