from django.test import TestCase
from django.urls import reverse

from users.models import CustomUser
from .models import Book , Genre


# Create your tests here.
class BooksTestCase(TestCase):
    def test_no_books(self):
        response = self.client.get(reverse("books:books_list"))

        self.assertContains(response , "No books found.")

    def test_books_list(self):

        Book.objects.create(title = "Book title" ,
                            description = "Book description",
                            isbn = "37286320787",
                            language="English",
                            page_count=306,
                            genre=Genre.objects.create(genre_name="Fiction",
                                                       genre_slug="Fiction Books"),
                            cover_picture='books_image/18050143.jpg'
                            )
        Book.objects.create(title="2 - Book title",
                            description="2- Book description",
                            isbn="832938239292",
                            language="English",
                            page_count=306,
                            genre=Genre.objects.create(genre_name="Fiction",
                                                       genre_slug="Fiction Books"),
                            cover_picture="books_image/77264987.jpg"
                            )
        Book.objects.create(title="3 - Book title",
                            description="3- Book description",
                            isbn="129884936011",
                            language="English",
                            page_count=306,
                            genre=Genre.objects.create(genre_name="Fiction",
                                                       genre_slug="Fiction Books"),
                            cover_picture='books_image/3-kitob.jpg'
                            )

        response = self.client.get(reverse("books:books_list"))

        books = Book.objects.all()


        for book in books:
            self.assertContains(response , book.title)

    def test_detail_page(self):


        book = Book.objects.create(title = "Book title" ,
                            description = "Book description",
                            isbn = "37286320787",
                            language="English",
                            page_count=306,
                            genre=Genre.objects.create(genre_name="Fiction",
                                                        genre_slug="Fiction Books"),
                            cover_picture="books_image/2-kitob_sOLy40U.jpg"
                            )

        response = self.client.get(reverse("books:books_detail" ,kwargs={"pk":book.pk}))

        self.assertContains(response , book.title)
        self.assertContains(response , book.description)

    def test_search_books(self):

        book1 = Book.objects.create(title="Dasturlash",
                            description="Book description",
                            isbn="37286320787",
                            language="English",
                            page_count=306,
                            genre=Genre.objects.create(genre_name="Fiction",
                             genre_slug="Fiction Books"),
                            cover_picture='books_image/18050143.jpg'
                            )
        book2 = Book.objects.create(title="Kutubxona",
                            description="2- Book description",
                            isbn="832938239292",
                            language="English",
                            page_count=306,
                            genre=Genre.objects.create(genre_name="Fiction",
                             genre_slug="Fiction Books"),
                            cover_picture="books_image/77264987.jpg"
                            )
        book3 = Book.objects.create(title="Yodgorlik",
                            description="3- Book description",
                            isbn="129884936011",
                            language="English",
                            page_count=306,
                            genre=Genre.objects.create(genre_name="Fiction",
                             genre_slug="Fiction Books"),
                            cover_picture='books_image/3-kitob.jpg'
                            )

        response = self.client.get(reverse("books:books_list")+'?q=dasturlash')
        self.assertContains(response ,book1.title)
        self.assertNotContains(response , book2.title)
        self.assertNotContains(response, book3.title)

        response = self.client.get(reverse("books:books_list") + '?q=kutubxona')
        self.assertContains(response, book2.title)
        self.assertNotContains(response, book1.title)
        self.assertNotContains(response, book3.title)

        response = self.client.get(reverse("books:books_list") + '?q=yodgorlik')
        self.assertContains(response, book3.title)
        self.assertNotContains(response, book2.title)
        self.assertNotContains(response, book1.title)



class BookReviewTestCase(TestCase):
    def test_add_review(self):

        book = Book.objects.create(title="Books New ",
                            description="Book description",
                            isbn="37286320787",
                            language="English",
                            page_count=306,
                            genre=Genre.objects.create(genre_name="Triller",
                             genre_slug="Triller Books"),
                            cover_picture='books_image/18050143.jpg'
                            )

        user = CustomUser.objects.create(username="welicodev",
                                         first_name="Otabek",
                                         last_name="Xurramov",
                                         email="xurramovotabek568@gmail.com")
        user.set_password("somepassword")
        user.save()

        self.client.login(username="welicodev" , password="somepassword")

        self.client.post(reverse("books:books_reviews" , kwargs={"pk":book.pk}) , data={
            "stars_given":4,
            "comment":"Nice book"
        })

        book_reviews = book.bookreview_set.all()
        self.assertEqual(book_reviews.count() ,1)
        self.assertEqual(book_reviews[0].stars_given , 4)
        self.assertEqual(book_reviews[0].comment, "Nice book")
        self.assertEqual(book_reviews[0].book, book)
        self.assertEqual(book_reviews[0].user, user)

