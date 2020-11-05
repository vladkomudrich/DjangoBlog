from articles.models import Category

def common_context(request):
    return {'categories': Category.objects.all()}
