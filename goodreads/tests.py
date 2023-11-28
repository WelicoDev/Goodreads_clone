from django.test import TestCase
from django.urls import reverse

from books.models import Genre , Book , BookReview
from users.models import CustomUser


class HomePageTestCase(TestCase):
    def test_paginated_list(self):
        book = Book.objects.create(title="Book title",
                                   description="Book description",
                                   isbn="37286320787",
                                   language="English",
                                   page_count=306,
                                   genre=Genre.objects.create(genre_name="Fiction",
                                                              genre_slug="Fiction Books"),
                                   cover_picture="books_image/2-kitob_sOLy40U.jpg"
                                   )

        user = CustomUser.objects.create(username="welicodev",
                                         first_name="Otabek",
                                         last_name="Xurramov",
                                         email="xurramovotabek568@gmail.com")
        user.set_password("somepassword")
        user.save()

        self.client.login(username='welicodev', password='somepassword')

        review1 = BookReview.objects.create(book=book , user=user , stars_given=4 , comment="Very good book")
        review2 = BookReview.objects.create(book=book, user=user, stars_given=5, comment="Nice book")
        review3 = BookReview.objects.create(book=book, user=user, stars_given=3, comment="Useful book")

        response = self.client.get(reverse("home_page") + "?page_size=2")

        self.assertContains(response , review3.comment)
        self.assertContains(response , review2.comment)
        self.assertNotContains(response , review1.comment)