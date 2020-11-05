from django.http import HttpResponse
from django.shortcuts import render

from articles.models import Article

def home(request):
    articles = Article.objects.order_by('-date')
    return render(request, 'home.html', {'articles': articles, 'hide_description': True})

def topmonth(request):
    return render(request, 'topmonth.html')