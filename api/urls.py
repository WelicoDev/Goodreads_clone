from django.urls import path
from .views import BookReviewDetailAPIView , BookReviewListAPIView

# from rest_framework.routers import DefaultRouter
# from .views import BookReviewViewSet
app_name = 'api'
#
# router = DefaultRouter()
# router.register('reviews', BookReviewViewSet, basename='review')
# urlpatterns = router.urls


urlpatterns = [
    path('reviews/' , BookReviewListAPIView.as_view() , name='books_reviews_api'),
    path('reviews/<int:pk>/' , BookReviewDetailAPIView.as_view() , name='review_detail_api'),
]