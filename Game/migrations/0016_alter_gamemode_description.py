# Generated by Django 3.2.9 on 2021-12-02 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0015_auto_20211125_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamemode',
            name='description',
            field=models.CharField(max_length=500, verbose_name='Description'),
        ),
    ]
