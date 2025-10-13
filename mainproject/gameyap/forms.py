from django import forms
from .models import Game, UserProfile
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'avatar', 'favorite_games']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'favorite_games': forms.SelectMultiple(attrs={'class': 'form-control'})
        }

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'genre', 'release_date', 'description']
