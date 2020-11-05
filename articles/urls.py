from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('category/<slug>', views.category, name='category'),
    path('', views.article_list, name='list'),
    path('<slug>', views.article_detail, name='detail'),
]