import media
import fresh_tomatoes

# create 6 different movies to display in a web browser.
amazing_spider_man = media.Movie('The Amazing Spider-Man',
                                 'https://images-na.ssl-images-amazon.com/images/M/MV5BMjMyOTM4MDMxNV5BMl5BanBnXkFtZTcwNjIyNzExOA@@._V1_SY1000_CR0,0,674,1000_AL_.jpg',
                                 'https://www.youtube.com/watch?v=upwf8RsyNqQ')

deadpool = media.Movie('Deadpool',
                       'https://images-na.ssl-images-amazon.com/images/M/MV5BMjQyODg5Njc4N15BMl5BanBnXkFtZTgwMzExMjE3NzE@._V1_SY1000_SX686_AL_.jpg',
                       'https://www.youtube.com/watch?v=ONHBaC-pfsk')

bourne_identity = media.Movie('The Bourne Identity',
                              'https://images-na.ssl-images-amazon.com/images/M/MV5BM2JkNGU0ZGMtZjVjNS00NjgyLWEyOWYtZmRmZGQyN2IxZjA2XkEyXkFqcGdeQXVyNTIzOTk5ODM@._V1_SY1000_CR0,0,666,1000_AL_.jpg',
                              'https://www.youtube.com/watch?v=FpKaB5dvQ4g')

kill_bill = media.Movie('Kill Bill: Vol. 1',
                        'https://images-na.ssl-images-amazon.com/images/M/MV5BMTU1NDg1Mzg4M15BMl5BanBnXkFtZTYwMDExOTc3._V1_.jpg',
                        'https://www.youtube.com/watch?v=7kSuas6mRpk')

the_hangover = media.Movie('The Hangover',
                           'https://images-na.ssl-images-amazon.com/images/M/MV5BMTU1MDA1MTYwMF5BMl5BanBnXkFtZTcwMDcxMzA1Mg@@._V1_.jpg',
                           'https://www.youtube.com/watch?v=tcdUhdOlz9M')

unforgiven = media.Movie('Unforgiven',
                         'https://images-na.ssl-images-amazon.com/images/M/MV5BODM3YWY4NmQtN2Y3Ni00OTg0LWFhZGQtZWE3ZWY4MTJlOWU4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,665,1000_AL_.jpg',
                         'https://www.youtube.com/watch?v=ftTX4FoBWlE')

movies = [amazing_spider_man, deadpool, bourne_identity, kill_bill,
          the_hangover, unforgiven]

# display movies in web browser
fresh_tomatoes.open_movies_page(movies)
