from django.test import TestCase
from rango.models import Category

class CategoryMethodTests(TestCase):
    def test_slug_line_creation(self):
        category = Category(name='Test Category String')
        category.save()
        self.assertEqual(category.slug, 'test-category-string')
