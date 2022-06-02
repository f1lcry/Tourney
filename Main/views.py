from django.db.models import Q
from django.shortcuts import render
from Game.models import GameMode


def index(request):
    title = "Главная"
    tourney_description = "Уже этой зимой на каникулах проходит первый киберспортивный " \
                          "турнир Лицея 64 Приморского района! Турнир будет проводиться полностью дистанционно. " \
                          "Он включает в себя целых 6 различных дисциплин, начиная со всеми известного " \
                          "Counter Strike Global Offensive, заканчивая скоростным поиском в интернете! " \
                          "Да-да, у нас будет и такое! На нашем сайте Вам будет " \
                          "предоставлена информация о большинстве из дисциплин. А также здесь " \
                          "будут опубликовываться итоги."
    how_to_play = "Если Вы игрок и были зарегистрированы заранее, то Вам нужно подать заявку. Там Вам нужно будет " \
                  "предоставить основную информацию о себе, такую как имя и возраст, а также оставить ссылки на " \
                  "социальные сети и почту для связи с организатором."
    team_description = "Наша команда делится на 2 группы: организаторы и разработчики. " \
                       "Организаторы - это двигатель нашей команды. Именно они берут всю работу по организации " \
                       "турнира на себя. Они составляют сетки, планируют матчи, проводят мозговые штурмы в целях " \
                       "выявления новых идей для внедрения в турнир и контролируют игры, чтобы всё было по-честному. " \
                       "Разработчики же проливают свет на всю работу организаторов, " \
                       "продвигая турнир в массы при помощи сайта."
    game_desc = "На турнире будут проводиться матчи в 6 дисциплинах. " \
                "Слева представлены самые популярные из них. "
    game_modes = {
        "CS:GO": GameMode.objects.get(name="CS:GO 5v5").description,
        "Clash Royale": GameMode.objects.get(name="Clash Royale 1v1").description,
        "Dota 2": GameMode.objects.get(name="Dota 2").description
    }

    context = {
        "title": title,
        "tourney_description": tourney_description,
        "how_to_play": how_to_play,
        "games": game_modes,
        "team_description": team_description,
        "game_desc": game_desc,
    }
    return render(request, 'Main/index.html', context)


def results(request):
    title = "Итоги"
    context = {
        'title': title
    }

    return render(request, 'Main/results.html', context)


