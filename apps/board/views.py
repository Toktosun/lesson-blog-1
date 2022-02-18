from django.http import HttpResponse
from django.shortcuts import render

from apps.board.models import PublicationAd


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
    response = render(request, 'index.html')
    return response
