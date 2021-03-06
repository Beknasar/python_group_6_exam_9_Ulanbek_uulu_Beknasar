# Generated by Django 2.2.13 on 2020-10-24 05:27

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
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='user_pics', verbose_name='Аватар')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='photos', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
        ),
    ]
