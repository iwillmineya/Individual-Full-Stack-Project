# Generated migration to add user field to Game model

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gameyap', '0005_game_is_active_gamemedia'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='games', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
