from itertools import count

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
# from django.views.generic import ListView , DetailView
from .forms import BookReviewForm
from .models import Book, BookReview, Genre
from users.models import CustomUser
# Create your views here.


# class BookListView(ListView):
#     template_name = 'books/list.html'
#     queryset = Book.objects.all()
#     context_object_name = "books"
#     paginate_by = 5


class BookListView(View):
    def get(self , request):
        books = Book.objects.all().order_by("pk")
        search_query = request.GET.get('q' , '')
        if search_query:
            books = books.filter(title__icontains=search_query)

        page_size = request.GET.get('page_size' , 5)
        paginator = Paginator(books , page_size)

        page_num = request.GET.get('page' ,1)
        page_obj = paginator.get_page(page_num)

        context = {
            "page_obj":page_obj,
            "search_query":search_query,
        }
        return render(request , 'books/list.html' , context)


# class BookDetailView(DetailView):
#     template_name = 'books/views.html'
#     queryset = Book.objects.all()
#     context_object_name = "book"


class BookDetailView(View):
    def get(self , request , pk):
        book = Book.objects.get(pk=pk)
        review_form = BookReviewForm()

        review_all = book.bookreview_set.all()
        sum = 0
        for i in review_all:
            sum+=i.stars_given

        review_count = review_all.count()
        if review_count > 0:
            rating = round(sum/review_count)

        else:
            rating = 0

        rating_full = [x for x in range(rating)]
        rating_empty = [x for x in range(5-rating)]

        context = {
            "book":book,
            "review_form":review_form,
            "rating":rating,
            "rating_full":rating_full,
            "rating_empty":rating_empty,
        }

        return render(request , "books/views.html" , context)


class AddReviewView(LoginRequiredMixin ,View):
    def post(self , request , pk):
        book = Book.objects.get(pk=pk)
        review_form = BookReviewForm(data=request.POST)
        context = {
            "book": book,
            "review_form": review_form,
        }

        if review_form.is_valid():
            BookReview.objects.create(
                book = book,
                user = request.user,
                stars_given=review_form.cleaned_data['stars_given'],
                comment = review_form.cleaned_data['comment']
            )
            return redirect(reverse("books:books_detail",kwargs={"pk":book.pk}))

        return render(request, "books/views.html", context)

class EditReviewView(LoginRequiredMixin , View):
    def get(self , request , book_id , review_id):
        book = Book.objects.get(pk=book_id)
        review = book.bookreview_set.get(pk=review_id)
        review_form = BookReviewForm(instance=review)
        context = {
            "book":book,
            "review":review,
            "review_form": review_form,
        }
        return render(request , 'books/edit_review.html' , context)

    def post(self , request , book_id , review_id):
        book = Book.objects.get(pk=book_id)
        review = book.bookreview_set.get(pk=review_id)
        review_form = BookReviewForm(instance=review , data=request.POST)

        if review_form.is_valid():
            review_form.save()

            return redirect(reverse("books:books_detail", kwargs={"pk": book.pk}))

        context = {
            "book": book,
            "review": review,
            "review_form": review_form,
        }

        return render(request, 'books/edit_review.html', context)


class ConfirmDeleteReview(LoginRequiredMixin , View):
    def get(self , request , book_id , review_id):
        books = Book.objects.all().order_by("pk")
        book = Book.objects.get(pk=book_id)
        review = book.bookreview_set.get(pk=review_id)

        context = {
            "books":books,
            "book": book,
            "review": review,
        }
        return render(request , 'books/confirm_delete.html' ,context)

class DeleteView(LoginRequiredMixin , View):
    def get(self , request , book_id , review_id):
        book = Book.objects.get(pk=book_id)
        review = book.bookreview_set.get(pk=review_id)

        review.delete()
        messages.success(request , "You have successfully deleted this review")

        return redirect(reverse("books:books_detail", kwargs={"pk": book.pk}))

class GenreView(LoginRequiredMixin , View):
    def get(self , request):
        genre_list = Genre.objects.all()
        context = {
            "genre_list": genre_list,
        }

        return render(request , 'books/genre.html' ,context)

