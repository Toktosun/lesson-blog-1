from apps.social.models import ArticleCategory


def article_category_list(request):
    category_qs = ArticleCategory.objects.all()
    return {'category_list': category_qs}
