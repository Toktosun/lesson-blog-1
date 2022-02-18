from django.http import HttpResponse
from django.shortcuts import render

from apps.board.models import PublicationAd
from apps.social.models import Article


def show_board(request):
    """показ доски объявлений"""
    publications = PublicationAd.objects.all()
    response = render(
        request,
        'ad-list.html',
        context={'publication_list': publications}
    )
    return response


def show_all_articles(request):
    """Показ всех артиклей"""
    article_qs = Article.objects.all()
    response = render(request, 'index.html',
                      context={'article_list': article_qs})
    return response
