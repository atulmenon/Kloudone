# Generated by Django 3.0.3 on 2020-07-13 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movie_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=500)),
                ('release_date', models.DateTimeField(verbose_name='Released on')),
            ],
        ),
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_budget', models.CharField(max_length=50)),
                ('movie_revenue', models.CharField(max_length=50)),
                ('movie_review', models.CharField(max_length=10)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NewDemo.movie_list')),
            ],
        ),
    ]
