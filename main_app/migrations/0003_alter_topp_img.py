# Generated by Django 4.1.7 on 2023-04-10 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_joke'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topp',
            name='img',
            field=models.URLField(default='url', max_length=500),
        ),
    ]
