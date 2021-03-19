from django.shortcuts import render, HttpResponse, redirect
from books_author_app.models import *

# Create your views here.

def index(request):
    return render (request, 'home2.html')

def books(request):
    context = {
        'books_all': Book.objects.all()
    }
    return render(request, 'home.html', context)

def authors(request):
    context = {
        'authors_all': Author.objects.all()
    }
    return render(request, 'Author.html', context)

def add_book(request):
    title = request.POST['title']
    description = request.POST['desc']
    Book.objects.create(title = title, desc = description)
    return redirect('/books')

def add_author(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    notes = request.POST['notes']
    Author.objects.create(first_name = first_name, last_name= last_name, notes=  notes)
    return redirect('/authors')

def show_author(request, author_id):
    author = Author.objects.get(id = author_id)
    context = {
        'author': author,
        'books': Book.objects.exclude(authors__id = author_id)
    }
    return render (request, 'show_author.html', context )
    

def show_book(request, book_id):
    book = Book.objects.get(id = book_id)
    context = {
        "book" : book, 
        "authors": Author.objects.exclude(books__id = book_id),
    }
    return render (request, "book.html", context)

def add_author_to_book(request,book_id):
    book = Book.objects.get(id=book_id)
    author = Author.objects.get(id=request.POST['author_id'])
    book.authors.add(author)
    return redirect(f'/show_book/{book_id}')

def add_book_to_author (request,author_id):
    author = Author.objects.get(id = author_id)
    book = Book.objects.get(id = request.POST['book_id'])
    author.books.add(book)
    return redirect(f'/show_author/{author_id}')