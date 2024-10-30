from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    is_gover = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} ({self.city})'


class Book(models.Model):
    title = models.CharField(max_length=100, unique=True)
    published_date = models.DateField()
    pages = models.IntegerField(default=0, null=False)
    description = models.TextField(blank=True)
    author = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits = 10, decimal_places=2, default=0)
    rating = models.DecimalField(max_digits = 10, decimal_places=2, null=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='publisher', null=True)

    def __str__(self):
        return f'{self.title} ({self.published_date.year})'


    
