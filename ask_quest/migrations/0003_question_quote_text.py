# Generated by Django 2.2.12 on 2020-12-19 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask_quest', '0002_question_responsed'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='quote_text',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
