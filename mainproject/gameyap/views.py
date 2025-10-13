from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Game
from .forms import GameForm

def home(request):
    games = Game.objects.all()
    featured_games = Game.objects.order_by('-release_date')[:3]
    leaderboard_ow = [
        "Proper", "Smurf", "Fleta", "Lip", "Fearless", "Hanbin", "ChoiSehwan", "Shu", "Viol2t", "Leave"
    ]
    leaderboard_val = [
        "Derke", "TenZ", "Sacy", "aspas", "Leo", "Boaster", "Less", "MaKo", "Zyppan", "cNed"
    ]
    return render(request, "index.html", {
        "games": games,
        "featured_games": featured_games,
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


from django.views.decorators.http import require_POST

@login_required
@require_POST
def game_like(request, pk):
    game = get_object_or_404(Game, pk=pk)
    game.likes += 1
    game.save()
    return redirect("home")

@login_required
@require_POST
def game_dislike(request, pk):
    game = get_object_or_404(Game, pk=pk)
    game.dislikes += 1
    game.save()
    return redirect("home")