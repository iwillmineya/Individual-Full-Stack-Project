from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Game, UserProfile
from .forms import GameForm, UserProfileForm

@login_required
def profile_view(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, "profile.html", {"profile": profile})

@login_required
def profile_edit(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile_view")
    else:
        form = UserProfileForm(instance=profile)
    return render(request, "profile_edit.html", {"form": form})

def home(request):
    search_query = request.GET.get('search', '')
    genre_query = request.GET.get('genre', '')
    release_query = request.GET.get('release_date', '')
    games = Game.objects.all()
    if search_query:
        games = games.filter(title__icontains=search_query)
    if genre_query:
        games = games.filter(genre=genre_query)
    if release_query:
        games = games.filter(release_date=release_query)
    genres = Game.objects.values_list('genre', flat=True).distinct()
    leaderboard_ow = [
        "Proper", "Smurf", "Fleta", "Lip", "Fearless", "Hanbin", "ChoiSehwan", "Shu", "Viol2t", "Leave"
    ]
    leaderboard_val = [
        "Derke", "TenZ", "Sacy", "aspas", "Leo", "Boaster", "Less", "MaKo", "Zyppan", "cNed"
    ]
    context = {
        'games': games,
        'genres': genres,
        'search_query': search_query,
        'genre_query': genre_query,
        'release_query': release_query,
        'leaderboard_ow': leaderboard_ow,
        'leaderboard_val': leaderboard_val,
    }
    return render(request, 'index.html', context)

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




    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'likes': game.likes, 'dislikes': game.dislikes, 'status': status})
    return redirect("home")