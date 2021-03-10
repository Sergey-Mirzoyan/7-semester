from catalog.models import Author, Genre, Language, Book
from django.contrib.auth.models import User
from django.contrib import admin
# import django

# class AdminBuilder():
#     def __init__(self):
#         self.reset()
#
#     def reset(self):
#         self.email = None
#         self.password = None
#         self.is_staff = True
#
#     @property
#     def product(self):
#         if not self.email:
#             self.email = 'authenticated@smth.com'
#         if not self.password:
#             self.password = 'Igor'
#         if not self.is_staff:
#             self.is_staff = True
#
#         product = django.contrib.admin.ModelAdmin.create(email=self.email, password=self.password, is_staff=self.is_staff)
#         self.reset()
#         return product
#
#     def setup(self, first_name=None, last_name=None, date_of_birth=None, date_of_death=None):
#         if isinstance(email, str):
#             self.email = email
#         if isinstance(password, str):
#             self.last_name = password



class UserBuilder():
    def __init__(self):
        self.reset()

    def reset(self):
        self.email = None
        self.password = None
        self.is_staff = False

    @property
    def product(self):
        if not self.email:
            self.email = 'authenticated@smth.com'
        if not self.password:
            self.password = 'Igor'
        if not self.is_staff:
            self.is_staff = False

        product = User.objects.create(email=self.email, password=self.password, is_staff=self.is_staff)
        self.reset()
        return product

    def setup(self, first_name=None, last_name=None, date_of_birth=None, date_of_death=None):
        if isinstance(email, str):
            self.email = email
        if isinstance(password, str):
            self.last_name = password


class AuthorBuilder():

    def __init__(self):
        self.reset()

    def reset(self):
        self.first_name = None
        self.last_name = None
        self.date_of_birth = None
        self.date_of_death = None

    @property
    def product(self):
        if not self.first_name:
            self.first_name = 'Bob'
        if not self.last_name:
            self.last_name = 'Igor'
        if not self.date_of_birth:
            self.date_of_birth = '2020-11-06'
        if not self.date_of_death:
            self.date_of_death = '2120-11-06'

        product = Author.objects.create(first_name=self.first_name, last_name=self.last_name, date_of_birth=self.date_of_birth, date_of_death=self.date_of_death)
        self.reset()
        return product

    def setup(self, first_name=None, last_name=None, date_of_birth=None, date_of_death=None):
        if isinstance(first_name, str):
            self.first_name = first_name
        if isinstance(last_name, str):
            self.last_name = last_name
        if isinstance(date_of_birth, str):
            self.date_of_birth = date_of_birth
        if isinstance(date_of_death, str):
            self.date_of_death = date_of_death


class LanguageBuilder():

    def __init__(self):
        self.reset()

    def reset(self):
        self.name = None

    @property
    def product(self):
        if not self.name:
            self.name = 'Russian'

        product = Language.objects.create(name = self.name)
        self.reset()
        return product

    def setup(self, name=None):
        if isinstance(name, str):
            self.name = name


class GenreBuilder():

    def __init__(self):
        self.reset()

    def reset(self):
        self.name = None

    @property
    def product(self):
        if not self.name:
            self.name = 'Яой'

        product = Genre.objects.create(name=self.name)

        self.reset()
        return product

    def setup(self, name=None):
        if isinstance(name, str):
            self.name = name
###########################################################################
class BookBuilder():

    def __init__(self):
        self.reset()

    def reset(self):
        self.title = None
        self.author = None
        self.summary = None
        self.genre = set()
        self.isbn = None
        self.language = None

    @property
    def product(self):
        if not self.title:
            self.title = 'Master and Burito'
        if not self.author:
            self.author = self.build_author()
        if not self.summary:
            self.summary = '1000000$'
        if not self.genre:
            self.build_genre()
        if not self.isbn:
            self.isbn = '100ret3udsir47cr0000$'
        if not self.language:
            self.build_language()

        product = Book.objects.create(title=self.title, author=self.author, summary=self.summary, genre=self.genre, isbn=self.isbn, language=self.language)
        self.reset()
        return product.object

    def build_author(self, first_name=None, last_name=None, date_of_birth=None, date_of_death=None):
        builder = AuthorBuilder()
        builder.setup(first_name, last_name, date_of_birth, date_of_death)

        self.author = builder.product

    def build_genre(self, name=None):
        builder = GenreBuilder()
        builder.setup(name)

        self.genre = builder.product

    def build_language(self, name=None):
        builder = LanguageBuilder()
        builder.setup(name)

        self.language = builder.product

    def setup(self, title=None, author=None, summary=None, genre=None, isbn=None, language=None):
        if isinstance(title, str):
            self.title = title
        if isinstance(summary, str):
            self.summary = summary
        if isinstance(isbn, str):
            self.isbn = isbn


    #
    # builder = BookBuilder()
    # builder.setup(title = 'Master and Burito')
    # builder.build_author('Bob')
    # builder.build_genre('Manga')
    # builder.build_language('English')
    #
    # builder.product
    #
