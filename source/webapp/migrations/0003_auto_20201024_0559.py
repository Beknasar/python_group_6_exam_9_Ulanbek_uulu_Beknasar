# Generated by Django 2.2.13 on 2020-10-24 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20201024_0531'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'verbose_name': 'Фотография', 'verbose_name_plural': 'Фотографии'},
        ),
        migrations.RenameField(
            model_name='photo',
            old_name='photo',
            new_name='image',
        ),
    ]
