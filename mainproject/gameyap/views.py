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
    games = Game.objects.all()
    leaderboard_ow = [
        "Proper", "Smurf", "Fleta", "Lip", "Fearless", "Hanbin", "ChoiSehwan", "Shu", "Viol2t", "Leave"
    ]
    leaderboard_val = [
        "Derke", "TenZ", "Sacy", "aspas", "Leo", "Boaster", "Less", "MaKo", "Zyppan", "cNed"
    ]
    context = {
        'games': games,
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