from django.shortcuts import render
from .models import GameMode, Game


def index(request, game_mode_name=None, game_pk=None):
    title = "Games"
    context = {
        'title': title,
    }

    if game_pk:
        """ Game info page """

        title = "Game info"
        game = Game.objects.get(pk=game_pk)
        if game.game_mode.name[:5] == "CS:GO":
            is_csgo = True
        else:
            is_csgo = False
        is_modes = False
        is_info = True
        context = {
            'game': game,
            'title': title,
            'is_modes': is_modes,
            'is_info': is_info,
            'is_csgo': is_csgo
        }

    elif game_mode_name:
        """ List of games with each game mode """

        games = Game.objects.filter(game_mode__name=game_mode_name).order_by("-id")
        is_modes = False
        is_info = False
        title = game_mode_name
        context.update({
            'games': games,
            'is_modes': is_modes,
            'is_info': is_info,
            'game_mode': game_mode_name,
            'title': title,
        })
        # team1, team2 = games[0].get_stats()
        # print(team2[0].team)

    else:
        """ List of game modes """

        game_modes = GameMode.objects.order_by("name")
        is_modes = True
        is_info = False
        context = {
            'game_modes': game_modes,
            'is_modes': is_modes,
            'is_info': is_info,
        }

    return render(request, 'Game/index.html', context)
