from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    CAT = (('tanks', 'танки'),
           ('healers', 'хилеры'),
           ('damage_dealers', 'дамагеры'),
           ('dealers', 'торговцы'),
           ('gildmasters', 'гилдмастеры'),
           ('quest_givers', 'выдаватель квестов'),
           ('blacksmiths', 'кузнецы'),
           ('tanners', 'кожевники'),
           ('potion_makers', 'зельевары'),
           ('spell_masters', 'мастера заклинаний'))
    category = models.CharField(max_length=15, choices=CAT, verbose_name='категория')
    dateCreation = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=256, verbose_name='название')
    text = RichTextField()


class Response(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст')
    status = models.BooleanField(default=False)
    dateCreation = models.DateTimeField(auto_now_add=True)