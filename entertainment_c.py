# Importing necessary modules.
import media
import fresh_tomatoes

# Creating instances of the Movie Class.

a_b_mind = media.Movie("A Beautiful Mind",
                        " After John Nash, a brilliant but asocial mathematician"
                        ",accepts secret work in cryptography, his life takes"
                        " a turn for the nightmarish",
                        "https://www.youtube.com/watch?v=aS_d0Ayjw4o",
                        "https://upload.wikimedia.org/wikipedia/en/b/b8/A_Beautiful_Mind_Poster.jpg")
the_dark_night = media.Movie("The Dark Night",
                             "When the menace known as the Joker wreaks havoc"
                             " and chaos on the people of Gotham, the Dark Knight"
                             " must save the city.",
                             "https://www.youtube.com/watch?v=EXeTwQWrcwY",
                             "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg")
matrix = media.Movie("The Matrix",
                     "A computer hacker learns from mysterious rebels about"
                     " the true nature of his reality and his role in the war"
                     " against its controllers.",
                     "https://www.youtube.com/watch?v=vKQi3bBA1y8",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/c/c1/The_Matrix_Poster.jpg/220px-The_Matrix_Poster.jpg")

initial_d = media.Movie("Initial D: Third Stage",
                        "The thrilling world of Mountain pass Drifting(Animated)",
                        "https://www.youtube.com/watch?v=Es_JcmKolis",
                        "http://vignette2.wikia.nocookie.net/voiceacting/images/d/d1/Initial_D_Third_Stage_DVD_Cover.jpg/revision/latest?cb=20130909155403")
whiplash = media.Movie("Whiplash",
                       "A promising young drummer enrolls at a cut-throat"
                       "music conservatory",
                       "https://www.youtube.com/watch?v=7d_jQycdQGo",
                       "https://upload.wikimedia.org/wikipedia/en/0/01/Whiplash_poster.jpg")
limitless = media.Movie("Limitless",
                        "A man who gains the ability to use the full extent"
                        "of his brain's capabilities",
                        "https://www.youtube.com/watch?v=4TLppsfzQH8",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/17/Limitless_Poster.jpg/220px-Limitless_Poster.jpg")
burnt = media.Movie("Burnt",
                     "Adam Jones is a chef who destroyed his career with drugs"
                     " and diva behavior. He cleans up and returns",
                     "https://www.youtube.com/watch?v=QsyzkkI_g14",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/2/21/Burnt_Poster_Updated.jpg/220px-Burnt_Poster_Updated.jpg")


# Saving the instances on an array of movies.
movies = [a_b_mind, the_dark_night, matrix, initial_d, whiplash, limitless, burnt]

# Calling the method to generate and open the movies page with the array of movies as the argument.
fresh_tomatoes.open_movies_page(movies)
