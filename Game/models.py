from datetime import date

from django.db import models
# from Account.models import User


class GameMode(models.Model):
    name = models.CharField("Name", max_length=50)
    description = models.CharField("Description", max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Режим"
        verbose_name_plural = "Режимы"


class Game(models.Model):
    game_mode = models.ForeignKey(GameMode, null=False, on_delete=models.CASCADE)
    date = models.DateField("Date", default=date.today, blank=True)
    map = models.CharField("Map", max_length=50, blank=True)
    link_demo = models.URLField("Link to the demo game", blank=True)

    def get_teams(self):
        return Team.objects.filter(game__pk=self.pk).order_by("-is_winner")

    def is_csgo(self):
        if self.game_mode.name[:5] == "CS:GO" or self.game_mode.name == "Dota ":
            return 1
        return 0

    def is_user_winner(self, request):
        winner_team = self.get_teams()[0]
        winner_stats = UserStats.objects.filter(team__pk=winner_team.pk)
        for stat in request.user.get_stats():
            if stat in winner_stats:
                return 1
        return 0

    def __str__(self):
        return f"{self.date} {self.game_mode}"

    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"


class Team(models.Model):
    name = models.CharField("Team name", max_length=50, default="")
    score = models.PositiveSmallIntegerField("Team score", default=0)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    is_winner = models.BooleanField("Is team a winner", default=False)

    def __str__(self):
        return f"{self.name} {self.game.date}"

    def get_stats(self):
        return UserStats.objects.filter(team__pk=self.pk).order_by("-kills")

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"


class UserStats(models.Model):
    player = models.ForeignKey("Account.User", null=False, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)
    kills = models.PositiveSmallIntegerField("Убийства", null=True, blank=True)
    deaths = models.PositiveSmallIntegerField("Смерти", null=True, blank=True)
    assists = models.PositiveSmallIntegerField("Помощи", null=True, blank=True)

    def count_kd(self):
        if self.deaths == 0:
            return self.kills
        return round(self.kills / self.deaths, 2)

    def __str__(self):
        return f"{self.player.username} {self.team.name} {self.team.game.date}"

    class Meta:
        verbose_name = "Статистика игрока"
        verbose_name_plural = "Статистики игроков"
