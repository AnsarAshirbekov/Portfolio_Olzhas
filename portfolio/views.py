from django.shortcuts import render
from .models import Book

def about_me(request):
    return render(request, 'about_me.html')

def skills(request):
    return render(request, 'skills.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def books(request):
    books = Book.objects.all()
    context = {
        "books" : books
    }
    return render(request, 'books.html', context)