# Generated by Django 4.1.1 on 2022-10-03 11:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='имя')),
                ('last_name', models.CharField(max_length=30, verbose_name='фамилия')),
                ('vk_link', models.CharField(max_length=100, verbose_name='vk_link')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='код')),
                ('title', models.CharField(max_length=30, verbose_name='название')),
                ('author', models.CharField(max_length=100, verbose_name='автор')),
                ('genre', models.CharField(max_length=20, verbose_name='жанр')),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='shop.client', verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
                'ordering': ['title', 'author'],
            },
        ),
    ]
