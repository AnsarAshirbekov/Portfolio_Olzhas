from django.urls import path
from .views import about_me, skills, portfolio

urlpatterns = [
    path('', about_me, name='about_me'),
    path('skills', skills, name='skills'),
    path('portfolio', portfolio, name='portfolio')
]