from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView

from .models import Article, Category
from .forms import AddComment

def article_list(request):
    articles = Article.objects.order_by('-date')
    return render(request, 'articles/list.html', {'articles': articles}) 

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    try:
        next_article = article.get_next_by_date()
    except Article.DoesNotExist:
        next_article = None
    
    try:
        prev_article = article.get_previous_by_date()
    except Article.DoesNotExist:
        prev_article = None
    
    comments = article.comments.filter()
    if request.method == 'POST':
        data = request.POST.dict()
        form = AddComment(data=data, article=article)
        if form.is_valid():
            form.save()
    else:
        form = AddComment()
    return render(request, 'articles/detail.html', {
        'article': article,
        'next_article': next_article,
        'prev_article': prev_article,
        'comments': comments, 
        'form': form,
    })

def category(request, slug):
    category = Category.objects.get(slug=slug)
    articles = category.articles.order_by('-date')
    return render(request, 'articles/list.html', {'category': category, 'articles': articles})