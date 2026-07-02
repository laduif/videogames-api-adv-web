from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Game
from .serializers import GameSerializer
from django.shortcuts import render, redirect
from .forms import GameForm

def home(request):

    return render(request, "games/home.html")

@api_view(['GET'])
def get_all_games(request):

    games = Game.objects.all()
    serializer = GameSerializer(games, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def get_top_sales(request):

    games = Game.objects.order_by('-global_sales')[:20]

    serializer = GameSerializer(games, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def get_games_by_genre(request, genre):

    games = Game.objects.filter(genre=genre)

    serializer = GameSerializer(games, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def get_games_by_platform(request, platform):

    games = Game.objects.filter(platform=platform)

    serializer = GameSerializer(games, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def get_games_by_publisher(request, publisher):
    
    games = Game.objects.filter(publisher=publisher)

    serializer = GameSerializer(games, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def add_game(request):

    serializer = GameSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def game_form(request):

    if request.method == "POST":
        form = GameForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("all_games")
    else:
        form = GameForm()

    return render(request, "games/add_game.html", {"form": form})

