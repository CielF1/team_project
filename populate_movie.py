import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'django_team_project.settings')
import django

django.setup()
from rango.models import Category, Page

def populate():

    drama_movies = [
        {'title': 'Forrest Gump',
         'director': 'Robert Zemeckis',
         'actors': 'Tom Hanks, Rebecca Williams, Sally Field, Michael Conner Humphreys, Harold G. Herthum',
         'url':'https://www.imdb.com/title/tt0109830/?ref_=fn_al_tt_1/',
         'views': 90,
         'poster': 'movie_posters/Forrest_Gump.jpg',
         'description': "Forrest Gump is a simple man with a low I.Q. but good intentions. He is running through childhood with his best and only friend Jenny. His 'mama' teaches him the ways of life and leaves him to choose his destiny. Forrest joins the army for service in Vietnam, finding new friends called Dan and Bubba, he wins medals, creates a famous shrimp fishing fleet, inspires people to jog, starts a ping-pong craze, creates the smiley, writes bumper stickers and songs, donates to people and meets the president several times. However, this is all irrelevant to Forrest who can only think of his childhood sweetheart Jenny Curran, who has messed up her life. Although in the end all he wants to prove is that anyone can love anyone."},
        {'title': 'The Shawshank Redemption',
         'director': 'Frank Darabont',
         'actors': 'Tim Robbins, Morgan Freeman, Bob Gunton, William Sadler, Clancy Brown',
         'url':'https://www.imdb.com/title/tt0111161/?ref_=fn_al_tt_2/',
         'views': 100,
         'poster': 'movie_posters/The_Shawshank_Redemption.jpg',
         'description': "Chronicles the experiences of a formerly successful banker as a prisoner in the gloomy jailhouse of Shawshank after being found guilty of a crime he did not commit. The film portrays the man's unique way of dealing with his new, torturous life; along the way he befriends a number of fellow prisoners, most notably a wise long-term inmate named Red."},
        {'title': 'Hotel Rwanda',
         'director': 'Terry George',
         'actors': 'Don Cheadle, Sophie Okonedo',
         'url': 'https://www.imdb.com/title/tt0395169/?ref_=nv_sr_srsg_0',
         'views': 80,
         'poster': 'movie_posters/Hotel_Rwanda.jpg',
         'description': "Paul Rusesabagina, a hotel manager, houses over a thousand Tutsi refugees during their struggle against the Hutu militia in Rwanda, Africa."},
        {'title': 'Persian Lessons',
         'director': 'Vadim Perelman',
         'actors': 'Nahuel Pérez, BiscayartLars, EidingerJonas Nay',
         'url': 'https://www.imdb.com/title/tt9738784/?ref_=nv_sr_srsg_0/',
         'views': 80,
         'poster': 'movie_posters/Persian_Lessons.jpg',
         'description': "A young Jewish man pretends to be Iranian to avoid being executed in a concentration camp."},
        {'title': "Schindler's List",
         'director': 'Steven Spielberg',
         'actors': 'Liam Neeson, Ralph Fiennes, Ben Kingsley',
         'url': 'https://www.imdb.com/title/tt0108052/?ref_=nv_sr_srsg_0/',
         'views': 95,
         'poster': "movie_posters/Schindler's_List.jpg",
         'description': "In German-occupied Poland during World War II, industrialist Oskar Schindler gradually becomes concerned for his Jewish workforce after witnessing their persecution by the Nazis."},
    ]

    comedy_movies = [
        {'title': 'Deadpool',
         'director': 'Tim Miller',
         'actors': 'Ryan Reynolds, Karan Soni, Ed Skrein, Michael Benyaer, Stefan Kapicic',
         'url':'https://www.imdb.com/title/tt1431045/?ref_=fn_al_tt_1/',
         'views': 30,
         'poster': 'movie_posters/Deadpool.jpg',
         'description': "This is the origin story of former Special Forces operative turned mercenary Wade Wilson, who after being subjected to a rogue experiment that leaves him with accelerated healing powers, adopts the alter ego Deadpool. Armed with his new abilities and a dark, twisted sense of humor, Deadpool hunts down the man who nearly destroyed his life."},
        {'title': 'Paddington',
         'director': 'Paul King',
         'actors': 'Hugh Bonneville, Sally Hawkins, Brendan Gleeson, Julie Walters, Jim Broadbent',
         'url': 'https://www.imdb.com/title/tt1109624/?ref_=nv_sr_srsg_0',
         'views': 75,
         'poster': 'movie_posters/Paddington.jpg',
         'description': "A young Peruvian bear travels to London in search of a home. Finding himself lost and alone at Paddington Station, he meets the kindly Brown family, who offer him a temporary haven."},
        {'title': 'La vita è bella',
         'director': 'Roberto Benigni',
         'actors': 'Roberto Benigni, Nicoletta Braschi, Giorgio Cantarini',
         'url': 'https://www.imdb.com/title/tt0118799/?ref_=nv_sr_srsg_0/',
         'views': 90,
         'poster': 'movie_posters/Vitaebella.jpg',
         'description': "When an open-minded Jewish librarian and his son become victims of the Holocaust, he uses a perfect mixture of will, humor, and imagination to protect his son from the dangers around their camp."},
        {'title': 'The terminal',
         'director': 'Steven Spielberg',
         'actors': 'Tom Hanks, Catherine Zeta-Jones, Stanley Tucci',
         'url': 'https://www.imdb.com/title/tt0362227/?ref_=nv_sr_srsg_0/',
         'views': 95,
         'poster': 'movie_posters/the_terminal.jpg',
         'description': "An Eastern European tourist unexpectedly finds himself stranded in JFK airport, and must take up temporary residence there."},
        {'title': 'Night at the Museum',
         'director': 'Shawn Levy',
         'actors': 'Ben Stiller, Carla Gugino, Dick Van Dyke, Mickey Rooney, Bill Cobbs',
         'url': 'https://www.imdb.com/title/tt0477347/?ref_=nv_sr_srsg_0/',
         'views': 85,
         'poster': 'movie_posters/Night_at_the_Museum.jpg',
         'description': "A newly recruited night security guard at the Museum of Natural History discovers that an ancient curse causes the animals and exhibits on display to come to life and wreak havoc."},
    ]
    war_movies = [
        {'title': 'Dunkirk',
         'director': 'Christopher Nolan',
         'actors': 'Fionn Whitehead, Tom Glynn-Carney, Jack Lowden, Harry Styles, Aneurin Barnard',
         'url': 'https://www.imdb.com/title/tt5013056/?ref_=fn_al_tt_1/',
         'views': 70,
         'poster': 'movie_posters/Dunkirk.jpg',
         'description': "Allied soldiers from Belgium, the British Commonwealth and Empire, and France are surrounded by the German Army and evacuated during a fierce battle in World War II."},
        {'title': 'Hacksaw Ridge',
         'director': 'Mel Gibson',
         'actors': 'Andrew Garfield, Sam Worthington, Luke Bracey, Teresa Palmer, Hugo Weaving',
         'url': 'https://www.imdb.com/title/tt2119532/?ref_=fn_al_tt_1/',
         'views': 60,
         'poster': 'movie_posters/Hacksaw_Ridge.png',
         'description': "World War II American Army Medic Desmond T. Doss, who served during the Battle of Okinawa, refuses to kill people and becomes the first man in American history to receive the Medal of Honor without firing a shot."},
        {'title': "Billy Lynn's Long Halftime Walk",
         'director': 'Ang Lee',
         'actors': 'Joe Alwyn, Garrett Hedlund, Kristen Stewart, Vin Diesel, Steve Martin',
         'url': 'https://www.imdb.com/title/tt2513074/?ref_=nv_sr_srsg_0/',
         'views': 70,
         'poster': "movie_posters/Billy_Lynn's_Long_Halftime_Walk_poster.png",
         'description': "19-year-old Billy Lynn is brought home for a victory tour after a harrowing Iraq battle. Through flashbacks, the film shows what really happened to his squad - contrasting the realities of war with America's perceptions."},
        {'title': "Murphy's War",
         'director': 'Peter Yates',
         'actors': "Peter O'Toole, Siân Phillips",
         'url': 'https://www.imdb.com/title/tt0067458/?ref_=fn_al_tt_1/',
         'views': 70,
         'poster': "movie_posters/Murphy's_War.jpeg",
         'description': "A lone survivor from a British naval ship is obsessed with getting revenge on a German U-boat crew that massacred his shipmates in the water."},
        {'title': '1917',
         'director': 'Sam Mendes',
         'actors': 'Dean-Charles Chapman, George MacKay, Daniel Mays',
         'url': 'https://www.imdb.com/title/tt8579674/?ref_=nv_sr_srsg_0/',
         'views': 90,
         'poster': 'movie_posters/1917.jpeg',
         'description': "April 6th, 1917. As a regiment assembles to wage war deep in enemy territory, two soldiers are assigned to race against time and deliver a message that will stop 1,600 men from walking straight into a deadly trap."},
    ]
    sci_fi_movies = [
        {'title': 'Interstellar',
         'director': 'Christopher Nolan',
         'actors': 'Matthew McConaughey, Anne Hathaway, Jessica Chastain, Bill Irwin, Ellen Burstyn',
         'url': 'https://www.imdb.com/title/tt0816692/?ref_=nv_sr_srsg_0/',
         'views': 90,
         'poster': 'movie_posters/Interstellar.jpg',
         'description': "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival."},
        {'title': 'Inception',
         'director': 'Christopher Nolan',
         'actors': 'Ken Watanabe, Joseph Gordon-Levitt, Marion Cotillard, Elliot Page, Tom Hardy',
         'url': 'https://www.imdb.com/title/tt1375666/?ref_=nv_sr_srsg_0/',
         'views': 85,
         'poster': 'movie_posters/Inception.jpg',
         'description': "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O."},
        {'title': 'Annihilation',
         'director': 'Alex Garland',
         'actors': 'Natalie Portman, Jennifer Jason Leigh, Gina Rodriguez, Tessa Thompson, Tuva Novotny',
         'url': 'https://www.imdb.com/title/tt2798920/?ref_=nv_sr_srsg_0/',
         'views': 70,
         'poster': 'movie_posters/Annihilation.png',
         'description': "A biologist signs up for a dangerous, secret expedition into a mysterious zone where the laws of nature don't apply."},
        {'title': 'Blade Runner 2049',
         'director': 'Denis Villeneuve',
         'actors': 'Ryan Gosling, Harrison Ford, Ana de Armas, Sylvia Hoeks, Robin Wright',
         'url': 'https://www.imdb.com/title/tt1856101/?ref_=nv_sr_srsg_0/',
         'views': 75,
         'poster': 'movie_posters/Blade_Runner_2049.png',
         'description': "Young Blade Runner K's discovery of a long-buried secret leads him to track down former Blade Runner Rick Deckard, who's been missing for thirty years."},
        {'title': 'Under the Skin',
         'director': 'Jonathan Glazer',
         'actors': 'Scarlett Johansson, Jeremy McWilliams, Lynsey Taylor Mackay',
         'url': 'https://www.imdb.com/title/tt1441395/?ref_=nv_sr_srsg_0/',
         'views': 65,
         'poster': 'movie_posters/IUnder_the_skin.png',
         'description': "A mysterious young woman seduces lonely men in the evening hours in Scotland. However, events lead her to begin a process of self-discovery."},
    ]
    cats = {'Drama': {'movies': drama_movies, 'views': 128, 'likes': 64},
            'Comedy': {'movies': comedy_movies, 'views': 64, 'likes': 32},
            'War': {'movies': war_movies, 'views': 32, 'likes': 16},
            'Science fiction': {'movies': sci_fi_movies, 'views': 76, 'likes': 54}}

    for cat, cat_data in cats.items():
        c = add_cat(cat,views=cat_data['views'], likes=cat_data['likes'])
        for p in cat_data['movies']:
            add_page(c, p['title'], p['director'], p['actors'],
                     p['url'], views=p['views'], poster=p['poster'], description=p['description'])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_page(cat,title,director,actors,url,views=0,poster='movie_posters/Default_poster.jpg',description=''):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.director = director
    p.actors = actors
    p.url=url
    p.views=views
    p.poster=poster
    p.description=description
    p.save()
    return p

def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c

if __name__=='__main__':
    print('Starting Rango population script...')
    populate()