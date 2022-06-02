# Generated by Django 3.2.9 on 2021-11-25 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0014_auto_20211125_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstats',
            name='assists',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Помощи'),
        ),
        migrations.AlterField(
            model_name='userstats',
            name='deaths',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Смерти'),
        ),
        migrations.AlterField(
            model_name='userstats',
            name='kills',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Убийства'),
        ),
    ]