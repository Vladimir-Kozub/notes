# Generated by Django 2.2.6 on 2019-11-03 20:07

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='md_field',
            field=markdownx.models.MarkdownxField(default=''),
        ),
    ]
