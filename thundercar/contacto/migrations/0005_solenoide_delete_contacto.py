# Generated by Django 4.2.8 on 2023-12-13 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0004_rename_project_contacto'),
    ]

    operations = [
        migrations.CreateModel(
            name='solenoide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido', models.CharField(max_length=200)),
                ('nombre', models.CharField(max_length=30)),
                ('dni', models.IntegerField()),
                ('fecNac', models.DateField()),
                ('email', models.EmailField(max_length=100)),
                ('adjuntar', models.ImageField(upload_to='')),
                ('consulta', models.TextField(max_length=250)),
            ],
        ),
        migrations.DeleteModel(
            name='contacto',
        ),
    ]