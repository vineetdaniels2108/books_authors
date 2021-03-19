from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book),
    path('show_book/<int:book_id>', views.show_book),
    path('add_author_to_book/<int:book_id>/assign', views.add_author_to_book),
    path('books', views.books),
    path('authors', views.authors),
    path('add_author', views.add_author),
    path('show_author/<int:author_id>', views.show_author),
    path('add_book_to_author/<int:author_id>/assign', views.add_book_to_author)
]
