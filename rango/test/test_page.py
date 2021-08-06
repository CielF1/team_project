from django.test import TestCase
from rango.models import Page

class CategoryMethodTests(TestCase):
    # ensure the movie title is not none
    def test_page(self):
        page = Page(title=None)
        page.test()
        self.assertEqual((page.title is not None), True)