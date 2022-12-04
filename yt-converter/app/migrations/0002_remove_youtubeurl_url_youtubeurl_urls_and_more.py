# Generated by Django 4.1.2 on 2022-10-23 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='youtubeurl',
            name='url',
        ),
        migrations.AddField(
            model_name='youtubeurl',
            name='urls',
            field=models.TextField(default=1989, verbose_name='URL'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='youtubeurl',
            name='create_day',
            field=models.DateTimeField(auto_now_add=True, verbose_name='コンバート実行日'),
        ),
    ]