from django.shortcuts import render
from .models import Book
from django.db.models import Avg, Count, Min, Max, Sum

def about_me(request):
    return render(request, 'about_me.html')

def skills(request):
    return render(request, 'skills.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def books(request):
    books_all = Book.objects.all()
    books_first = Book.objects.first()
    books_last = Book.objects.last()
    books_get = Book.objects.get(title = 'Хроники Нарний')
    books_filter_publisher = Book.objects.filter(publisher__name = 'Бразука')
    books_date = Book.objects.filter(published_date__year__gte = 1995)
    books_agreg = Book.objects.aggregate(Avg('rating'))

    max_pages = Book.objects.aggregate(Max('pages'))
    book_max_pages = Book.objects.filter(pages = max_pages['pages__max'])
    
    book_oldest = Book.objects.aggregate(Min('published_date'))
    book_oldest_name = Book.objects.filter(published_date = book_oldest['published_date__min'])

    pages_quantity = Book.objects.aggregate(Sum('pages'))

    books_quantity = Book.objects.aggregate(Count('title'))

    context = {
        "books_all" : books_all,
        "books_first" : books_first,
        "books_last" : books_last,
        "books_get" : books_get,
        "books_filter_publisher" : books_filter_publisher,
        "books_date" : books_date,
        "books_agreg" : books_agreg,
        "book_max_pages" : book_max_pages,
        "book_oldest_name" : book_oldest_name,
        "pages_quantity" : pages_quantity,
        "books_quantity" : books_quantity,
    }
    return render(request, 'books.html', context)
    