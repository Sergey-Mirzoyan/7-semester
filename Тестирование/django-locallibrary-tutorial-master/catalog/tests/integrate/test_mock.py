from django.test import TestCase
from django.test.client import RequestFactory
from rest_framework import permissions
from catalog.models import Author, Language, Genre, Book
from catalog.views import AuthorListView, BookListView
from unittest.mock import patch
#from django.contrib.auth.models import User
from catalog.tests.integrate.databuilder import *
import django

class PermissionTest(TestCase):
    @classmethod
    def setUp(self):
        builder = UserBuilder()
        product = builder.product

        # admin_user = AdminBuilder()
        # admin = admin_user.product

    def test_authenticated_permisiion(self):
        #authenticated_user = User.objects.create(email='authenticated@smth.com', password='password03', is_staff=False)
        authenticated_user = django.contrib.auth.models.User.objects.get(id=1)
        factory = RequestFactory()
        request = factory.post('/catalog/authors')
        request.user = authenticated_user
        permission = permissions.IsAuthenticatedOrReadOnly()
        has_permission = permission.has_permission(request, AuthorListView)
        self.assertTrue(has_permission)


    @patch ("django.contrib.auth.models.User.objects.create")
    def london_url(self, mocked_method):
        User = django.contrib.auth.models.User.objects.get(id=1)
        mocked_method.assert_called_with('/catalog/authors', args=["1"])


    def test_user_has_no_permisiion(self):
        # authenticated_user_02 = User.objects.create(email='authenticate02d@smth.com', password='password03', is_staff=False)
        authenticated_user_02 = django.contrib.auth.models.User.objects.get(id=1)
        factory = RequestFactory()
        request = factory.post('/catalog/books')
        request.user = authenticated_user_02
        permission = permissions.IsAdminUser()
        has_permission = permission.has_permission(request, BookListView)
        self.assertFalse(has_permission)

    @patch ("django.contrib.auth.models.User.objects.create")
    def london_url(self, mocked_method):
        User = django.contrib.auth.models.User.objects.get(id=1)
        mocked_method.assert_called_with('/catalog/authors', args=["1"])



    #
    # def test_admin_permisiion(self):
    #     # admin_user = User.objects.create(email='admin@smth.com', password='password02', is_staff=True)
    #     admin_user = django.contrib.admin.objects.get(id=1)
    #     factory = RequestFactory()
    #     request = factory.post('/catalog/books')
    #     request.admin = admin_user
    #     permission = permissions.IsAdminUser()
    #     has_permission = permission.has_permission(request, BookListView)
    #     self.assertTrue(has_permission)
    #
    # @patch ("django.contrib.admin.objects.create")
    # def london_url(self, mocked_method):
    #     User = django.contrib.admin.objects.get(id=1)
    #     mocked_method.assert_called_with('/catalog/authors', args=["1"])
