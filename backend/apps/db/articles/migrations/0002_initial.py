# Generated by Django 4.2 on 2023-04-12 12:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postunlike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unlikes', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AddField(
            model_name='postlike',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='articles.post', verbose_name='post'),
        ),
        migrations.AddField(
            model_name='postlike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AddField(
            model_name='post',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='creator'),
        ),
        migrations.AddField(
            model_name='post',
            name='users_liked',
            field=models.ManyToManyField(related_name='post_liked', through='articles.PostLike', to=settings.AUTH_USER_MODEL, verbose_name='likes'),
        ),
        migrations.AddField(
            model_name='post',
            name='users_unliked',
            field=models.ManyToManyField(related_name='post_unliked', through='articles.PostUnlike', to=settings.AUTH_USER_MODEL, verbose_name='unlikes'),
        ),
    ]