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
         ]

    comedy_movies = [
        {'title': 'Deadpool',
         'director': 'Tim Miller',
         'actors': 'Ryan Reynolds, Karan Soni, Ed Skrein, Michael Benyaer, Stefan Kapicic',
         'url':'https://www.imdb.com/title/tt1431045/?ref_=fn_al_tt_1/',
         'views': 30,
         'poster': 'movie_posters/Deadpool.jpg',
         'description': "This is the origin story of former Special Forces operative turned mercenary Wade Wilson, who after being subjected to a rogue experiment that leaves him with accelerated healing powers, adopts the alter ego Deadpool. Armed with his new abilities and a dark, twisted sense of humor, Deadpool hunts down the man who nearly destroyed his life."},
         ]

    cats = {'Drama': {'movies': drama_movies, 'views': 128, 'likes': 64},
            'Comedy': {'movies': comedy_movies, 'views': 64, 'likes': 32}}

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