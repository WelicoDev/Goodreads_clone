from django.utils import timezone

from users.models import CustomUser
from django.core.validators import MinValueValidator , MaxValueValidator
from django.db import models

# Create your models here.

class Genre(models.Model):
    genre_name = models.CharField(max_length=200)
    genre_slug = models.CharField(max_length=200)

    def __str__(self):
        return self.genre_name
class Book(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    isbn = models.CharField(max_length=17)
    language = models.CharField(max_length=200)
    page_count = models.IntegerField()
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE)
    cover_picture = models.ImageField(default="default_cover.jpg" ,upload_to='books_image')

    def __str__(self):
        return self.title


class Author(models.Model):
    username = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    born = models.CharField(max_length=200)
    email = models.EmailField()
    bio = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class BookAuthor(models.Model):
    book = models.ForeignKey(Book , on_delete=models.CASCADE)
    author = models.ForeignKey(Author , on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book} - {self.author}"



class BookReview(models.Model):
    user = models.ForeignKey(CustomUser , on_delete=models.CASCADE)
    book = models.ForeignKey(Book , on_delete=models.CASCADE)
    comment = models.TextField()
    stars_given = models.IntegerField(
        validators=[MinValueValidator(1) , MaxValueValidator(5)]
    )

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comment[:200]

