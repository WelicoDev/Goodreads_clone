from django.urls import path
from .views import BookListView , BookDetailView , AddReviewView , EditReviewView , ConfirmDeleteReview , DeleteView , GenreView

app_name = "books"
urlpatterns = [
    path('' , BookListView.as_view() , name="books_list"),
    path('<int:pk>/' , BookDetailView.as_view() , name="books_detail"),
    path('<int:pk>/review/' , AddReviewView.as_view() , name="books_reviews"),
    path('<int:book_id>/reviews/<int:review_id>/edit/' , EditReviewView.as_view() , name='edit_review'),
    path('<int:book_id>/reviews/<int:review_id>/confirm/' , ConfirmDeleteReview.as_view() , name='confirm_review'),
    path('<int:book_id>/reviews/<int:review_id>/delete/' , DeleteView.as_view() , name='delete_review'),
    path('genre/' , GenreView.as_view() , name='genres_list'),
]