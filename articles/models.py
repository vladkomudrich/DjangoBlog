import pytils
import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)
    description = models.TextField(blank=True, max_length=250)
    keywords = models.TextField(blank=True, max_length=100)
    body = RichTextUploadingField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, db_index=True)
    thumb = models.ImageField(default='default.png', blank=True)
    altfield = models.CharField(max_length=100, default='image-description', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    categories = models.ManyToManyField('Category', blank=True, related_name='articles')

    def __str__(self):
        return self.title

    @property
    def was_published_recently(self):
        return self.date >= (timezone.now() - datetime.timedelta(days = 7))

    def get_absolute_url(self):
        return reverse('post', args=[str(self.slug)])

    def snippet(self): # use it for articles list
        return self.body[:150] + '...'

    def save(self, *args, **kwargs):
        if not self.slug.strip():
            self.slug = pytils.translit.slugify(self.title)
        return super().save(*args, **kwargs)

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author_name = models.CharField('Prénom', max_length=50)
    author_email = models.EmailField('Email', max_length=50)
    comment_text = models.CharField('Texte', max_length=200)
    date = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.comment_text

    @property
    def human_date(self):
        # Dec 16, 2017 @ 23:05
        return self.date.strftime('%b %e, %Y @ %H:%M')


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(blank=True)
    describe = models.TextField(blank=False, max_length = 350)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug.strip():
            self.slug = pytils.translit.slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post', args=[str(self.slug)])

    class Meta:
        verbose_name_plural = 'Categories'
