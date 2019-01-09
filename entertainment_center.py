import fresh_tomatoes
import media

Ralph = media.movie("Ralph breaks the Internet",
                        "A story of boy who breaks internet",
                        "https://upload.wikimedia.org/wikipedia/en/0/0b/Ralph_Breaks_the_Internet_%282018_film_poster%29.png",
                        "https://www.youtube.com/watch?v=DIBw9dSVKdU")
#print(toy_story.storyline)
robo = media.movie("Robo",
                   "robo will kill the bird man",
                   "https://upload.wikimedia.org/wikipedia/en/c/cf/2.0_film_poster.jpg",
                   "https://www.youtube.com/watch?v=2wvq8hdGdAw")
  
#print(robo.storyline)
#robo.show_trailer()
rangasthalam = media.movie("Rangasthalam",
                           "about a village history",
                           "https://upload.wikimedia.org/wikipedia/en/5/5d/Rangasthalam.jpg",
                           "https://www.youtube.com/watch?v=sueMmTm-M4Y")

bahubali = media.movie("Bahubali",
                       "movie about the war",
                       "https://upload.wikimedia.org/wikipedia/en/f/f9/Baahubali_the_Conclusion.jpg",
                       "https://www.youtube.com/watch?v=exOm83dRQUM")

bharath = media.movie("Bharath Ane Naenu",
                      "movie about politics",
                      "https://upload.wikimedia.org/wikipedia/en/6/68/Bharat_Ane_Nenu_poster.jpg",
                      "https://www.youtube.com/watch?v=orkPrGSAETs")

mission = media.movie("Mission Impossible",
                      "movie about spy",
                      "https://upload.wikimedia.org/wikipedia/en/3/3c/Missionimpossibleblurayboxset.jpg",
                      "https://www.youtube.com/watch?v=wb49-oV0F78")

movies = [Ralph,robo,rangasthalam,bahubali,bharath,mission]
fresh_tomatoes.open_movies_page(movies)
                           

           
