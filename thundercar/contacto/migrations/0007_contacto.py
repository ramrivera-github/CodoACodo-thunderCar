# Generated by Django 5.0 on 2023-12-14 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0006_alter_solenoide_adjuntar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido', models.CharField(max_length=200)),
                ('nombre', models.CharField(max_length=30)),
                ('dni', models.IntegerField()),
                ('fecNac', models.DateField()),
                ('email', models.EmailField(max_length=100)),
                ('adjuntar', models.FileField(upload_to='')),
                ('consulta', models.TextField(max_length=250)),
            ],
        ),
    ]
