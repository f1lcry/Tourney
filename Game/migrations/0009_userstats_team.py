# Generated by Django 3.2.9 on 2021-11-22 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0008_auto_20211122_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstats',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Game.team'),
        ),
    ]