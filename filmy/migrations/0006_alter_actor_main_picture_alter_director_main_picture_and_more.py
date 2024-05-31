# Generated by Django 5.0.4 on 2024-05-31 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmy', '0005_movie_actors_movie_description_movie_director_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='main_picture',
            field=models.CharField(blank=True, default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='director',
            name='main_picture',
            field=models.CharField(blank=True, default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='movie',
            name='main_picture',
            field=models.CharField(blank=True, default='', max_length=2000),
        ),
    ]
