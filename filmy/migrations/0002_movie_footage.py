# Generated by Django 5.0.4 on 2024-04-05 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='footage',
            field=models.PositiveSmallIntegerField(blank=True, help_text='in minutes', null=True),
        ),
    ]
