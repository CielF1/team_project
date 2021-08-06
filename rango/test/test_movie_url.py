from django.test import TestCase
from rango.models import Page

class CategoryMethodTests(TestCase):
    # ensure the movie url is not none, if the url is none, rango should return to index page
    def test_movie_url(self):
        page = Page(url=None)
        page.test()
        self.assertEqual((page.url is not None), True)