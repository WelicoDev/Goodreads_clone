from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from books.models import Book, Genre, BookReview
from users.models import CustomUser


# Create your tests here.
class BookReviewAPITEstCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username="welicodev",
                                              first_name="Otabek",
                                              last_name="Xurramov",
                                              email="xurramovotabek568@gmail.com")
        self.user.set_password("somepassword")
        self.user.save()
        self.client.login(username='welicodev',password='somepassword')



    def test_book_review_detail(self):
        book = Book.objects.create(title="Book title",
                                   description="Book description",
                                   isbn="37286320787",
                                   language="English",
                                   page_count=306,
                                   genre=Genre.objects.create(genre_name="Fiction",
                                                              genre_slug="Fiction Books"),
                                   cover_picture="books_image/2-kitob_sOLy40U.jpg"
                                   )

        book_review = BookReview.objects.create(book=book , user=self.user , stars_given=5 , comment="Very good book")

        response = self.client.get(reverse('api:review_detail_api' , kwargs={"pk": book_review.pk}))

        self.assertEqual(response.status_code , 200)
        self.assertEqual(response.data['id'] , book_review.id)
        self.assertEqual(response.data['stars_given'], 5)
        self.assertEqual(response.data['comment'], "Very good book")
        self.assertEqual(response.data['book']['id'] , book_review.book.id)
        self.assertEqual(response.data['book']['title'], book_review.book.title)
        self.assertEqual(response.data['book']['description'], book_review.book.description)
        self.assertEqual(response.data['book']['isbn'], book_review.book.isbn)
        self.assertEqual(response.data['user']['id'], book_review.user.id)
        self.assertEqual(response.data['user']['first_name'], book_review.user.first_name)
        self.assertEqual(response.data['user']['last_name'], book_review.user.last_name)
        self.assertEqual(response.data['user']['email'], book_review.user.email)
        self.assertEqual(response.data['user']['username'], book_review.user.username)

    def test_delete_review(self):
        book = Book.objects.create(title="Book title",
                                   description="Book description",
                                   isbn="37286320787",
                                   language="English",
                                   page_count=306,
                                   genre=Genre.objects.create(genre_name="Fiction",
                                                              genre_slug="Fiction Books"),
                                   cover_picture="books_image/2-kitob_sOLy40U.jpg"
                                   )

        book_review = BookReview.objects.create(book=book, user=self.user, stars_given=5, comment="Very good book")

        response = self.client.delete(reverse('api:review_detail_api',kwargs={'pk':book_review.pk}))

        self.assertEqual(response.status_code , 204)
        self.assertFalse(BookReview.objects.filter(pk=book_review.pk).exists())

    def test_patch_review(self):
        book = Book.objects.create(title="Book title",
                                   description="Book description",
                                   isbn="37286320787",
                                   language="English",
                                   page_count=306,
                                   genre=Genre.objects.create(genre_name="Fiction",
                                                              genre_slug="Fiction Books"),
                                   cover_picture="books_image/2-kitob_sOLy40U.jpg"
                                   )

        book_review = BookReview.objects.create(book=book, user=self.user, stars_given=5, comment="Very good book")
        response = self.client.patch(reverse('api:review_detail_api', kwargs={'pk': book_review.pk}) , data={'stars_given':4})

        self.assertEqual(response.status_code , 200)
        self.assertEqual(book_review.stars_given , 5)

    def test_put_review(self):
        book = Book.objects.create(title="Book title",
                                   description="Book description",
                                   isbn="37286320787",
                                   language="English",
                                   page_count=306,
                                   genre=Genre.objects.create(genre_name="Fiction",
                                                              genre_slug="Fiction Books"),
                                   cover_picture="books_image/2-kitob_sOLy40U.jpg"
                                   )

        book_review = BookReview.objects.create(book=book, user=self.user, stars_given=5, comment="Very good book")
        response = self.client.put(reverse('api:review_detail_api', kwargs={'pk': book_review.pk}) ,
                                   data={'stars_given':5 , 'comment':'Nice book' ,'user_id':self.user.pk , 'book_id':book.pk}
                                   )

        book_review.refresh_from_db()

        self.assertEqual(response.status_code , 200)
        self.assertEqual(book_review.stars_given , 5)
        self.assertEqual(book_review.comment , 'Nice book')

    def test_create_review(self):
        book = Book.objects.create(title="Book title",
                                   description="Book description",
                                   isbn="37286320787",
                                   language="English",
                                   page_count=306,
                                   genre=Genre.objects.create(genre_name="Fiction",
                                                              genre_slug="Fiction Books"),
                                   cover_picture="books_image/2-kitob_sOLy40U.jpg"
                                   )
        data = {
            'stars_given':3,
            'comment':'Nice book',
            'user_id':self.user.pk,
            'book_id':book.pk,
        }

        response = self.client.post(reverse('api:books_reviews_api') , data=data)
        book_review = BookReview.objects.get(book=book)

        self.assertEqual(response.status_code , 201)
        self.assertEqual(book_review.stars_given , 3)
        self.assertEqual(book_review.comment , 'Nice book')



    def test_book_review_list(self):
        user2 = CustomUser.objects.create(username="jewel",
                                         first_name="Javohir",
                                         last_name="Namazov",
                                         email="namazovjavohir044@gmail.com")
        book = Book.objects.create(title="Book title",
                                   description="Book description",
                                   isbn="37286320787",
                                   language="English",
                                   page_count=306,
                                   genre=Genre.objects.create(genre_name="Fiction",
                                                              genre_slug="Fiction Books"),
                                   cover_picture="books_image/2-kitob_sOLy40U.jpg"
                                   )

        book_review = BookReview.objects.create(book=book, user=self.user, stars_given=5, comment="Very good book")
        book_review2 = BookReview.objects.create(book=book, user=user2, stars_given=4, comment="Nice book")

        response = self.client.get(reverse('api:books_reviews_api'))

        self.assertEqual(response.status_code , 200)
        self.assertEqual(response.data['count'] , 2)
        self.assertIn('next' , response.data)
        self.assertIn('previous' , response.data)
        self.assertEqual(len(response.data['results']) , 2)
        self.assertEqual(response.data['results'][0]['id'] , book_review.id)
        self.assertEqual(response.data['results'][0]['stars_given'], book_review.stars_given)
        self.assertEqual(response.data['results'][0]['comment'], book_review.comment)
        self.assertEqual(response.data['results'][1]['id'], book_review2.pk)
        self.assertEqual(response.data['results'][1]['stars_given'], book_review2.stars_given)
        self.assertEqual(response.data['results'][1]['comment'], book_review2.comment)



