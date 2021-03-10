from django.test import *
from unittest.mock import patch
from catalog.tests.unittests.databuilder import *
# Create your tests here.

from catalog.models import Author


class AuthorModelTest(TestCase):

    @classmethod
    def setUp(self):
        """Set up non-modified objects used by all test methods."""
        # Author.objects.create(first_name='Big', last_name='Bob')
        builder = AuthorBuilder()
        product = builder.product

    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(author.get_absolute_url(), '/catalog/author/1')

    @patch ("django.urls.reverse")
    def london_url(self, mocked_method):
        author = Author.objects.get(id=1)
        mocked_method.assert_called_with('author-detail', args=["1"])
