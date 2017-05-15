import fresh_tomatoes
import media


toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://youtu.be/QW0sjQFpXTU")
#print(toy_story.storyline)
Moana = media.Movie("Moana",
                    "A story of a girl and a man that helps the green",
                    "https://s-media-cache-ak0.pinimg.com/236x/0b/aa/31/0baa317b04030e357d1bd687a52cfce9.jpg",
                    "https://youtu.be/LKFuXETZUsI")
#print(Moana.storyline)
Spy_Kids3 = media.Movie("Spy Kids 3",
                        "A story of two spy kids that go into a 3D game and help their friends",
                        "http://images.fan-de-cinema.com/affiches/large/3d/59781.jpg",
                        "https://youtu.be/WvJoVBe9zwI")
#print(Spy_Kids3.storyline)
Boss_Baby = media.Movie("Boss Baby",
                        "A story of a baby that is trying to save other babies.",
                        "http://filmpulse.net/wp-content/uploads/2016/12/The-Boss-Baby-.jpg",
                        "https://youtu.be/wfvxTyFJOiU")
#print(Boss_Baby.storyline)
The_Secret_Life_of_Pets = media.Movie("The Secret Life of Pets",
                                      "A story of pets that have an amazing adventure.",
                                      "https://upload.wikimedia.org/wikipedia/en/6/64/The_Secret_Life_of_Pets_poster.jpg",
                                      "https://youtu.be/UZ4WBlveGfw")
#print(The_Secret_Life_of_Pets.storyline)
The_Lorax = media.Movie("The Lorax",
                        "A story of a creature that speaks for the trees",
                        "https://fanart.tv/fanart/movies/73723/movieposter/dr-seuss-the-lorax-53c4ef4dc08ac.jpg",
                        "https://youtu.be/1bHdzTUNw-4")
#print(The_Lorax.storyline)

movies =[toy_story, Moana, Spy_Kids3, Boss_Baby, The_Secret_Life_of_Pets, The_Lorax]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VAILD_RATINGS)
print(media.Movie.__doc__)
                        

                    
