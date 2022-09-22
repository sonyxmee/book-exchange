from django.db import models
from django.urls import reverse


class Book(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='код')
    title = models.CharField(max_length=30, verbose_name='название')
    author = models.CharField(max_length=100, verbose_name='автор')
    genre = models.CharField(max_length=20, verbose_name='жанр')
    def __str__(self):
        return f"книга: {self.title}, автор: {self.author}"

    def get_absolute_url(self):
        return reverse('books')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['title', 'author']

class User(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='код')
    name = models.CharField(max_length=30, verbose_name='имя')
    surname = models.CharField(max_length=30, verbose_name='фамилия')
    vk_link = models.CharField(max_length=100, verbose_name='vk_link')

    def __str__(self):
        return f"имя: {self.title}, фамилия: {self.author}"

    def get_absolute_url(self):
        return reverse('books')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['title', 'author']