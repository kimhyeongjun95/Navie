# Generated by Django 3.2.9 on 2021-11-25 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_code', models.IntegerField()),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_code', models.IntegerField()),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_code', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_code', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_code', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('plot', models.TextField(null=True)),
                ('release_date', models.CharField(max_length=50, null=True)),
                ('poster_path', models.TextField(null=True)),
                ('backdrop_path', models.TextField(null=True)),
                ('vote_average', models.FloatField()),
                ('actors', models.ManyToManyField(related_name='movies', to='movies.Actor')),
                ('directors', models.ManyToManyField(related_name='movies', to='movies.Director')),
                ('genres', models.ManyToManyField(related_name='movies', to='movies.Genre')),
                ('keywords', models.ManyToManyField(related_name='movies', to='movies.Keyword')),
            ],
        ),
    ]
