from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.sitemaps.views import sitemap
from django.contrib.flatpages.sitemaps import FlatPageSitemap
from django.conf.urls.static import static
from django.conf import settings

from .sitemaps import ArticleSitemap, StaticViewSitemap, CategorySitemap

from .views import home, topmonth
from articles import views as article_views

sitemaps = {
    'articles': ArticleSitemap,
    'static': StaticViewSitemap,
    'flatepages': FlatPageSitemap,
    'categories': CategorySitemap,
}

urlpatterns = [
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}),
    path('robots.txt/', include('robots.urls')),
    path('post/<slug>', article_views.article_detail, name='post'),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('articles/', include('articles.urls')),
    path('topmonth/', topmonth, name='topmonth'),
    path('pages', include('django.contrib.flatpages.urls')),
    path('', home, name='home'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)