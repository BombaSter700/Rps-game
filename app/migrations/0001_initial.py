# Generated by Django 5.1.2 on 2024-11-06 05:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='player', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bot_move', models.CharField(blank=True, max_length=50)),
                ('user_move', models.CharField(blank=True, max_length=50)),
                ('status', models.CharField(blank=True, max_length=50)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='score', to='app.player')),
                ('created_at',models.DateTimeField(auto_now_add=True))
            ],
        ),
    ]
