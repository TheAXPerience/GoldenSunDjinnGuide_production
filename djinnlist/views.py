from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .models import Collectible, Category

# Create your views here.
@api_view(["GET"])
@renderer_classes([JSONRenderer])
def index(request):
    game = int(request.GET.get('game', '0'))
    coltype = int(request.GET.get('coltype', '0'))
    chapter = int(request.GET.get('chapter', '0'))

    # begin query on Collectable model
    query = Collectible.objects.all()

    # filter by game
    if game > 0:
        query = query.filter(game=game)

    # filter by coltype (type)
    if coltype > 0:
        query = query.filter(coltype=coltype)

    # filter by chapter
    if chapter > 0:
        query = query.filter(chapter=chapter)

    query = query.order_by('id')

    # go through query and serialize to ans
    context = []

    for c in query:
        context.append(c.serialize())

    ret = Response(context)

    # may need CORS header?

    return ret

"""
def by_game(request, game):
    return Response("List by game")

def by_type(request, game, coltype):
    return Response("List by game, of certain type")

def by_chapter(request, game, chapter):
    return Response("List by game, at certain part of game")
"""

@api_view(["GET"])
@renderer_classes([JSONRenderer])
def get_category(request, title):
    query = Category.objects.all().filter(game=title).order_by('id')
    context = []
    for c in query:
        context.append(c.serialize())
    ret = Response(context)

    return ret
