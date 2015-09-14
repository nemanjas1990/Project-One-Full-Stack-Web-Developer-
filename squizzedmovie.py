import movieslist
import basicmovie
import fresh_tomatoes
#import webbrowser

forrest_gump = movieslist.ForrestGump("Toy Story",
                        "A Story of a boy and his toys",
                        "http://ia.media-imdb.com/images/M/MV5BMTgwMjI4MzU5N15BMl5BanBnXkFtZTcwMTMyNTk3OA@@._V1_SY317_CR12,0,214,317_AL_.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        "John Lasseter")

inception = movieslist.Inception("Inception",
                        "A thief who steals corporate secrets through use of dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.",
                        "http://ia.media-imdb.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SX214_AL_.jpg",
                        "https://www.youtube.com/watch?v=66TuSJo4dZM",
                        "Christopher Nolan")

one_flew_over_the_cuckoo_nest = movieslist.OneFlewOvertheCuckoosNest("Flew Over Cuckoo's Nest",
                        "Upon admittance to a mental institution, a brash rebel rallies the patients to take on the oppressive head nurse.",
                        "http://ia.media-imdb.com/images/M/MV5BMTk5OTA4NTc0NF5BMl5BanBnXkFtZTcwNzI5Mzg3OA@@._V1_SY317_CR12,0,214,317_AL_.jpg",
                        "https://www.youtube.com/watch?v=azyK_k52R1w",
                        "Milos Forman")

shichinin_no_samurai = movieslist.Shichininnosamurai("Shichinin No Samurai",
                        "A Story of a boy and his toys",
                        "http://cdn.moviestillsdb.com/sm/3e4be28241c9ba194340ae4b25244d5b/shichinin-no-samurai.jpg",
                        "https://www.youtube.com/watch?v=azyK_k52R1w",
                        "y")

shawshank_redemption = movieslist.ShawshankRedemption("Shawshank Redemption",
                        "A Story of a boy and his toys",
                        "https://upload.wikimedia.org/wikipedia/sr/thumb/8/81/ShawshankRedemptionMoviePoster.jpg/250px-ShawshankRedemptionMoviePoster.jpg",
                        "https://www.youtube.com/watch?v=azyK_k52R1w",
                        "x")

godfather = movieslist.Godfather("Godfather",
                        "A Story of a boy and his toys",
                        "https://d12vb6dvkz909q.cloudfront.net/uploads/galleries/24681/the-godfather-1.jpg",
                        "https://www.youtube.com/watch?v=azyK_k52R1w",
                        "y")

dark_knight = movieslist.DarkKnight("Dark Knight",
                        "A Story of a boy and his toys",
                        "http://station79.files.wordpress.com/2012/07/the-dark-knight-rises-the-dark-knight-rises-30989937-1600-1200.jpg",
                        "https://www.youtube.com/watch?v=azyK_k52R1w",
                        "x")

schindlers_list = movieslist.SchindlersList("Schindler's List",
                        "A Story of a boy and his toys",
                        "http://7movie11.in/post91/Schindlers%20List%201993.jpg",
                        "https://www.youtube.com/watch?v=azyK_k52R1w",
                        "y")

pulp_fiction = movieslist.PulpFiction("Pulp Fiction",
                        "A Story of a boy and his toys",
                        "http://images.mentalfloss.com/sites/default/files/styles/article_640x430/public/pulpfiction.jpeg",
                        "https://www.youtube.com/watch?v=azyK_k52R1w",
                        "x")

il_buono_il_brutto_il_cattivo = movieslist.Ilbuonoilbruttoilcattivo("Il buono Il Brutto Il Cattivo",
                        "A Story of a boy and his toys",
                        "http://i.jeded.com/i/the-good-the-bad-and-the-ugly-il-buono-il-brutto-il-cattivo.9123.jpg",
                        "https://www.youtube.com/watch?v=azyK_k52R1w",
                        "y")

return_of_the_king = movieslist.ReturnoftheKing("Return of the King",
                        "A Story of a boy and his toys",
                        "http://www.glyphweb.com/arda/_images/soundtrack.jpg",
                        "https://www.youtube.com/watch?v=azyK_k52R1w",
                        "x")

fight_club = movieslist.FightClub("Fight Club",
                        "A Story of a boy and his toys",
                        "http://www.b92.net/news/pics/2015/02/22/27471677654ea2b26d22db301525535_orig.jpg",
                        "https://www.youtube.com/watch?v=azyK_k52R1w",
                        "y")

fellowship_of_the_ring = movieslist.FellowshipoftheRing("Fellowship of the Ring",
                        "A Story of a boy and his toys",
                        "http://img2.wikia.nocookie.net/__cb20070520010435/lotr/images/d/df/Fellowship1.jpg",
                        "https://www.youtube.com/watch?v=azyK_k52R1w",
                        "x")

empire_strikes_back = movieslist.EmpireStrikesBack("Empire Strikes Back",
                        "A Story of a boy and his toys",
                        "http://www.flickeringmyth.com/wp-content/uploads/2015/08/the-empire-strikes-back-dream-poster.jpg",
                        "https://www.youtube.com/watch?v=azyK_k52R1w",
                        "y")


movies = [forrest_gump, inception, one_flew_over_the_cuckoo_nest
          ,shichinin_no_samurai, shawshank_redemption, godfather, dark_knight
          ,schindlers_list, pulp_fiction, il_buono_il_brutto_il_cattivo
          ,return_of_the_king, fight_club, fellowship_of_the_ring, empire_strikes_back]
#print(movies)
#fresh_tomatoes.open_movies_page(movies)



#imitation_game.show_trailer()
#movies = [toy_story, avatar, imitation_game]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.__doc__)
