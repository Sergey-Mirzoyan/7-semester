from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import RequestFactory
from rest_framework import permissions
from catalog.models import Author, Language, Genre, Book
from catalog.views import AuthorListView, BookListView


class PermissionTest(TestCase):

    def test_authenticated_permisiion(self):
        #
        authenticated_user = User.objects.create(email='authenticated@smth.com', password='password03', is_staff=False)
        #authenticated_user = User.objects.get(id=1)
        factory = RequestFactory()
        request = factory.post('/catalog/authors')
        request.user = authenticated_user
        permission = permissions.IsAuthenticatedOrReadOnly()
        has_permission = permission.has_permission(request, AuthorListView)
        self.assertTrue(has_permission)

    def test_admin_permisiion(self):
        admin_user = User.objects.create(email='admin@smth.com', password='password02', is_staff=True)
        factory = RequestFactory()
        request = factory.post('/catalog/books')
        request.user = admin_user
        permission = permissions.IsAdminUser()
        has_permission = permission.has_permission(request, BookListView)
        self.assertTrue(has_permission)

    def test_user_has_no_permisiion(self):
        authenticated_user_02 = User.objects.create(email='authenticate02d@smth.com', password='password03', is_staff=False)
        factory = RequestFactory()
        request = factory.post('/catalog/books')
        request.user = authenticated_user_02
        permission = permissions.IsAdminUser()
        has_permission = permission.has_permission(request, BookListView)
        self.assertFalse(has_permission)
