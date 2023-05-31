from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(
        max_length=64,
        verbose_name='Название книги'
    )
    author = models.CharField(
        max_length=32,
        verbose_name='Автор'
    )
    publication_year = models.IntegerField(
        verbose_name='Год издательства'
    )
    price = models.FloatField(
        verbose_name='Цена'
    )
