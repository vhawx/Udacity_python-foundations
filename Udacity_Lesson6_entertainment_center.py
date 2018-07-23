import Udacity_Lesson6_media #this connections to the "media" file
import fresh_tomatoes

#media = other python folder Movie = class in other file.
harold_and_maude = Udacity_Lesson6_media.Movie("Harold and Maude",
                                        "Cult classic pairs Cort as a dead-pan disillusioned 20-year-old obsessed with suicide and a loveable Gordon as a fun-loving 80-year-old eccentric. They meet at a funeral, and develop a taboo romantic relationship, in which they explore the tired theme of the meaning of life with a fresh perspective.",
                                        "https://upload.wikimedia.org/wikipedia/en/5/5f/Harold_and_Maude_%281971_film%29_poster.jpg",
                                        "https://www.youtube.com/watch?v=u-cOukYeGVM")
#print(harold_and_maude.storyline)

some_like_it_hot = Udacity_Lesson6_media.Movie("Some Like it Hot",
                                     '''After witnessing a Mafia murder, slick saxophone player Joe (Tony Curtis) and his long-suffering buddy, Jerry (Jack Lemmon), improvise a quick plan to escape from Chicago with their lives. Disguising themselves as women, they join an all-female jazz band and hop a train bound for sunny Florida. While Joe pretends to be a millionaire to win the band's sexy singer, Sugar (Marilyn Monroe), Jerry finds himself pursued by a real millionaire (Joe E. Brown) as things heat up and the mobsters close in.''',
                                        "https://upload.wikimedia.org/wikipedia/en/b/b4/Some_Like_It_Hot_poster.jpg",
                                        "https://www.youtube.com/watch?v=rI_lUHOCcbc") 
#print(some_like_it_hot.storyline)

annie_hall = Udacity_Lesson6_media.Movie("Annie Hall",
                                        "Comedian Alvy Singer (Woody Allen) examines the rise and fall of his relationship with struggling nightclub singer Annie Hall (Diane Keaton). Speaking directly to the audience in front of a bare background, Singer reflects briefly on his childhood and his early adult years before settling in to tell the story of how he and Annie met, fell in love, and struggled with the obstacles of modern romance, mixing surreal fantasy sequences with small moments of emotional drama.",
                                        "https://upload.wikimedia.org/wikipedia/en/e/e6/Anniehallposter.jpg",
                                        "https://www.youtube.com/watch?v=OqVgCfZX-yE")
#print(annie_hall.storyline)
#annie_hall.show_trailer()
#use the object annie_hall to call the show_trailer method

#put the movies in an array
movies = [harold_and_maude, some_like_it_hot, annie_hall]
##display the movies on a webpage
#fresh_tomatoes.open_movies_page(movies) #provide movies as an argument to .open_movies_page function
print(Udacity_Lesson6_media.Movie.VALID_RATINGS)
