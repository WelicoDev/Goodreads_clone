from django.contrib import admin
from books.models import Book , Author , BookAuthor , BookReview , Genre

# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    list_display = ('genre_name' , 'genre_slug')
class BookAdmin(admin.ModelAdmin):
    list_display = ('title' , 'isbn' , 'description')
    search_fields = ('title', 'isbn')


class AuthorAdmin(admin.ModelAdmin):
    pass

class BookAuthorAdmin(admin.ModelAdmin):
    pass

class BookReviewAdmin(admin.ModelAdmin):
    pass


admin.site.register(Genre,GenreAdmin)
admin.site.register(Book , BookAdmin)
admin.site.register(Author , AuthorAdmin)
admin.site.register(BookAuthor , BookAuthorAdmin)
admin.site.register(BookReview , BookReviewAdmin)


