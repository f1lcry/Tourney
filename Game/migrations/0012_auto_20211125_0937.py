# Generated by Django 3.2.9 on 2021-11-25 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0011_auto_20211125_0935'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game',
            options={'verbose_name': 'Игра', 'verbose_name_plural': 'Игры'},
        ),
        migrations.AlterModelOptions(
            name='gamemode',
            options={'verbose_name': 'Режим', 'verbose_name_plural': 'Режимы'},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'verbose_name': 'Команда', 'verbose_name_plural': 'Команды'},
        ),
        migrations.AlterModelOptions(
            name='userstats',
            options={'verbose_name': 'Статистика игрока', 'verbose_name_plural': 'Статистики игроков'},
        ),
    ]