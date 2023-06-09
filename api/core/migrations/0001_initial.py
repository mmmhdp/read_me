# Generated by Django 4.2.1 on 2023-05-30 21:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('second_n', models.CharField(blank=True, max_length=200)),
                ('last_n', models.CharField(blank=True, max_length=200)),
                ('alias', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('summary', models.TextField()),
                ('global_genre', models.CharField(choices=[('fiction', 'fiction'), ('non-fiction', 'non-fiction')], default='written', max_length=100)),
                ('author', models.ManyToManyField(related_name='book', to='core.author')),
            ],
        ),
        migrations.CreateModel(
            name='PubInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisher', models.CharField(blank=True, max_length=200)),
                ('year', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='SubGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('description', models.CharField(blank=True, max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(blank=True)),
                ('rate', models.IntegerField(blank=True, default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='note', to=settings.AUTH_USER_MODEL)),
                ('related_paper', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='note', to='core.book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='pub_info',
            field=models.ForeignKey(blank=True, on_delete=models.SET('no info'), related_name='book', to='core.pubinfo'),
        ),
        migrations.AddField(
            model_name='book',
            name='sub_genre',
            field=models.ForeignKey(blank=True, on_delete=models.SET('no info'), related_name='book', to='core.subgenre'),
        ),
    ]
