# Generated by Django 3.0.3 on 2020-07-13 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewDemo', '0002_auto_20200713_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='movie_budget',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='details',
            name='movie_revenue',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='details',
            name='movie_review',
            field=models.CharField(max_length=500),
        ),
    ]
