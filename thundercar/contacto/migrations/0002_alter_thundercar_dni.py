# Generated by Django 4.2.8 on 2023-12-13 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thundercar',
            name='dni',
            field=models.IntegerField(),
        ),
    ]
