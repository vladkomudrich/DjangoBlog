from django.contrib.sitemaps import Sitemap, ping_google
from django.contrib.flatpages.models import FlatPage
from django.urls import reverse
from articles.models import Article, Category

class StaticViewSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5
    
    def items(self):
        return ['topmonth', 'home']

    def location(self, item):
        return reverse(item)

    def save(self, force_insert=False, force_update=False):
        super().save(force_insert, force_update)
        try:
            ping_google(sitemap_url = '/sitemap.xml')
        except Exception:
            pass

class FlatPageSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return FlatPage.objects.all()

    def save(self, force_insert=False, force_update=False):
        super().save(force_insert, force_update)
        try:
            ping_google(sitemap_url = '/sitemap.xml')
        except Exception:
            pass

class CategorySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return Category.objects.all()

    def save(self, force_insert=False, force_update=False):
        super().save(force_insert, force_update)
        try:
            ping_google(sitemap_url = '/sitemap.xml')
        except Exception:
            pass

class ArticleSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return Article.objects.all()

    def save(self, force_insert=False, force_update=False):
        super().save(force_insert, force_update)
        try:
            ping_google(sitemap_url = '/sitemap.xml')
        except Exception:
            pass