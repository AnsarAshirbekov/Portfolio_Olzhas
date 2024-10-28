from django.urls import path
from .views import about_me, skills, portfolio, books

urlpatterns = [
    path('', books, name='books'),
    path('skills', skills, name='skills'),
    path('portfolio', portfolio, name='portfolio'),
    path('about_me', about_me, name='about_me')
]