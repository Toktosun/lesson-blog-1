from django.db.models import Q
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.generic import TemplateView

from apps.board.models import PublicationAd
from apps.social.models import Article, ArticleCategory


# View бывают двух видов:
# 1. Function based view
# 2. Class based view


class BoardView(TemplateView):
    """Показ доски объявлений"""
    template_name = 'ad-list.html'

    def get_context_data(self, **kwargs):
        context = dict()
        context['publication_list'] = PublicationAd.objects.all()
        return context


class ArticleListView(TemplateView):
    """Показ всех артиклей"""
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = dict()
        query_parameters = self.request.GET  # dictionary
        search_word = str(query_parameters.get('search_word', None))
        if search_word:
            context['article_list'] = Article.objects.filter(
                Q(title__icontains=search_word) |
                Q(description__icontains=search_word) |
                Q(category__title__icontains=search_word)
            )
        else:
            context['article_list'] = Article.objects.all()
        return context


class ArticleSingleView(TemplateView):
    """Показ детальной страницы артикля"""
    template_name = 'single.html'

    def get_context_data(self, **kwargs):
        context = dict()
        try:
            article = Article.objects.get(id=kwargs['pk'])
        except Article.DoesNotExist:
            raise Http404
        context['article'] = article
        return context


# такая же view как BoardView, но через функцию
# def show_board(request):
#     """показ доски объявлений"""
#     publications = PublicationAd.objects.all()
#     response = render(
#         request,
#         'ad-list.html',
#         context={'publication_list': publications}
#     )
#     return response


# такая же view как ArticleListView, но через функцию
# def show_all_articles(request):
#     """Показ всех артиклей"""
#     article_qs = Article.objects.all()
#     response = render(request, 'index.html',
#                       context={'article_list': article_qs})
#     return response
