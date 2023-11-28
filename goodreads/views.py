from django.core.paginator import Paginator
from django.shortcuts import render

from books.models import BookReview


def landing_page(request):
    context = {}

    return render(request , 'landing_page.html' , context)

def home_page(request):
    book_review = BookReview.objects.all().order_by("-pk")
    page_size = request.GET.get('page_size', 10)
    paginator = Paginator(book_review , page_size)

    page_num = request.GET.get('page' , 1)
    page_object = paginator.get_page(page_num)
    context = {
        "book_review":book_review,
        "page_object":page_object,
    }

    return render(request , "home.html" , context)