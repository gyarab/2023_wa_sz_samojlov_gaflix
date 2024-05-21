from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmy', '0003_director_genre_rename_title_movie_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('birth_year', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True)),
                ('main_picture', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
