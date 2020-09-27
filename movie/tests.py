from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Movies
# Create your tests here.

class BlogTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='testuser', password='password')
        test_user.save()


        test_Movies = Movies.objects.create(
            author = test_user,
            title = 'sherlock',
            body = "Sherlock is a British crime television series based on Sir Arthur Conan Doyle's Sherlock Holmes detective stories."
        )
        test_Movies.save() 

        

    def test_Movies_content(self):

        movie = Movies.objects.get(id=1)
        actual_author = str(movie.author)
        actual_title = str(movie.title)
        actual_body = str(movie.body)

        self.assertEqual(actual_author, 'testuser')
        self.assertEqual(actual_title, 'sherlock')
        self.assertEqual(actual_body, "Sherlock is a British crime television series based on Sir Arthur Conan Doyle's Sherlock Holmes detective stories.")
