from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Client(models.Model):
    # id = models.IntegerField(primary_key=True, verbose_name='код')
    vk_link = models.CharField(max_length=100, verbose_name='vk_link')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return f"user: {self.user}"

    def get_absolute_url(self):
        return reverse('clients')
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['id']

class Book(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='код')
    title = models.CharField(max_length=30, verbose_name='название')
    author = models.CharField(max_length=100, verbose_name='автор')
    genre = models.CharField(max_length=20, verbose_name='жанр')
    # file will be uploaded to MEDIA_ROOT / uploads
    # image = models.ImageField(upload_to ='uploads/', blank=True, null=True)
    client = models.ForeignKey(Client, related_name='books', on_delete=models.CASCADE, verbose_name='пользователь')
    def __str__(self):
        return f"книга: {self.title}, автор: {self.author}"

    def get_absolute_url(self):
        return reverse('books')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['title', 'author']

