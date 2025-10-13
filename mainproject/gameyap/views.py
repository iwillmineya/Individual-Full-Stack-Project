from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Game
from .forms import GameForm

def home(request):
    games = Game.objects.all()
    leaderboard_ow = list(range(1, 11))  # Use 1-10 for demo, change to 501 for full
    leaderboard_val = list(range(1, 11))
    return render(request, "index.html", {
        "games": games,
        "leaderboard_ow": leaderboard_ow,
        "leaderboard_val": leaderboard_val,
    })

@login_required
def game_create(request):
    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = GameForm()
    return render(request, "game_form.html", {"form": form})

@login_required
def game_update(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if request.method == "POST":
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = GameForm(instance=game)
    return render(request, "game_form.html", {"form": form})

@login_required
def game_delete(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if request.method == "POST":
        game.delete()
        return redirect("home")
    return render(request, "game_confirm_delete.html", {"game": game})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def user_logout(request):
    logout(request)
    return redirect("home")