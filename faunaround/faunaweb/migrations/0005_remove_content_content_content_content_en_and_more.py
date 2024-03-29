# Generated by Django 4.1.7 on 2023-03-21 13:19

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('faunaweb', '0004_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='content',
        ),
        migrations.AddField(
            model_name='content',
            name='content_en',
            field=tinymce.models.HTMLField(blank=True, max_length=4000, null=True, verbose_name='content english'),
        ),
        migrations.AddField(
            model_name='content',
            name='content_national',
            field=tinymce.models.HTMLField(blank=True, max_length=4000, null=True, verbose_name='content national'),
        ),
    ]
