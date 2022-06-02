from django.db import models
from django.contrib.auth.models import AbstractUser
from Game.models import UserStats
from statistics import mean


class User(AbstractUser):
    # image = models.ImageField("User's image", blank=True)
    # gender = models.CharField("Gender", choices=genders, max_length=6)
    genders = [("male", "male"), ("female", "female")]
    age = models.PositiveIntegerField("Возраст на 01.01.2022", default=0)
    grade = models.CharField("Класс (если выпускник, указать)", max_length=15, default="")
    game_modes = models.ManyToManyField("Game.GameMode", related_name="Режимы")
    vk = models.URLField("Вконтакте", default="")
    is_player = models.BooleanField("Is user a player", default=False)

    def __str__(self):
        return self.username

    def get_stats(self):
        return UserStats.objects.filter(player__pk=self.pk)

    def get_games(self):
        stats = UserStats.objects.filter(player__pk=self.pk)
        games = []
        for stat in stats:
            games.append(stat.team.game)
        return games

    def get_win_rate(self):
        stats = UserStats.objects.filter(player__pk=self.pk)
        statuses = []
        for stat in stats:
            statuses.append(stat.team.is_winner)
        if statuses:
            return int(statuses.count(True) / len(statuses) * 100)
        return 0

    def get_av_kd(self):
        games = self.get_games()
        cs_games = []
        stats = UserStats.objects.filter(player__pk=self.pk)
        kds = []
        for game in games:  # Не в тему, но это сработало с первого раза
            if game.game_mode.name[:5] == "CS:GO":
                cs_games.append(game)
        for cs_game in cs_games:
            for stat in stats:
                if stat.team.game.pk == cs_game.pk:
                    kds.append(stat.count_kd())
        if kds:
            return round(mean(kds), 2)
        return 0

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
