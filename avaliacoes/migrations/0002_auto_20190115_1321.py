# Generated by Django 2.1.5 on 2019-01-15 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='data',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
