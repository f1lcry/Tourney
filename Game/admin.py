from django.contrib import admin
from .models import GameMode, UserStats, Game, Team


admin.site.register(UserStats)
admin.site.register(GameMode)
admin.site.register(Game)
admin.site.register(Team)
