from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from books.models import BookReview
from .serializers import BookReviewSerializers
from rest_framework import generics
from rest_framework import viewsets



#Create your views here.
class BookReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookReviewSerializers
    queryset = BookReview.objects.all()
    lookup_field = 'pk'

# class BookReviewDetailAPIView(APIView):
    # def get(self , request , pk):
    #     book_review = BookReview.objects.get(pk=pk)
    #     serializer = BookReviewSerializers(book_review)
    #
    #     return Response(data=serializer.data)
    #
    # def delete(self , request , pk):
    #     book_review = BookReview.objects.get(pk=pk)
    #     book_review.delete()
    #
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    #
    # def put(self , request , pk):
    #     book_review = BookReview.objects.get(pk=pk)
    #     serializer = BookReviewSerializers(instance=book_review , data=request.data)
    #
    #     if serializer.is_valid():
    #         serializer.save()
    #
    #         return Response(data=serializer.data , status=status.HTTP_200_OK)
    #
    #     return Response(data=serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    #
    # def patch(self, request, pk):
    #     book_review = BookReview.objects.get(pk=pk)
    #     serializer = BookReviewSerializers(instance=book_review, data=request.data , partial=True)
    #
    #     if serializer.is_valid():
    #         serializer.save()
    #
    #         return Response(data=serializer.data, status=status.HTTP_200_OK)
    #
    #     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # json_response = {
        #     "pk":book_review.pk,
        #     "stars_given":book_review.stars_given,
        #     "comment":book_review.comment,
        #     "book":{
        #         "id":book_review.book.pk,
        #         "title":book_review.book.title,
        #         "description":book_review.book.description,
        #         "isbn":book_review.book.isbn
        #     },
        #     "user":{
        #         "pk":book_review.user.pk,
        #         "first_name":book_review.user.first_name,
        #         "last_name":book_review.user.last_name,
        #         "username":book_review.user.username
        #     }
        # }

        # return JsonResponse(json_response)

# class BookReviewViewSet(viewsets.ModelViewSet):
#     serializer_class = BookReviewSerializers
#     queryset = BookReview.objects.all().order_by('-created_at')
#     lookup_field = 'pk'

class BookReviewListAPIView(generics.ListCreateAPIView):
    serializer_class = BookReviewSerializers
    queryset = BookReview.objects.all().order_by('-created_at')

# class BookReviewListAPIView(APIView):
#     def get(self , request):
#         books_reviews = BookReview.objects.all().order_by('-created_at')
#
#         paginator = PageNumberPagination()
#         page_objects = paginator.paginate_queryset(books_reviews , request)
#
#         serializer = BookReviewSerializers(page_objects , many=True)
#
#         return paginator.get_paginated_response(serializer.data)
#
#     def post(self , request):
#         serializer = BookReviewSerializers(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#
#             return Response(data=serializer.data , status=status.HTTP_201_CREATED)
#
#         return Response(data=serializer.errors , status=status.HTTP_400_BAD_REQUEST)
