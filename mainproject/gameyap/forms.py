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
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Game Title'}),
            'genre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Genre (e.g., Action, RPG)'}),
            'release_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'placeholder': 'YYYY-MM-DD'
            }),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Game description'}),
        }
        help_texts = {
            'release_date': 'Use date format: YYYY-MM-DD (e.g., 2024-12-05)',
        }
