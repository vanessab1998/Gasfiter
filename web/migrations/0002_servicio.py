# Generated by Django 4.0.3 on 2024-04-18 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('images', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Imagen')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='Descripción')),
                ('descriptionn', models.CharField(blank=True, max_length=500, null=True, verbose_name='Descripción')),
                ('descriptionnn', models.CharField(blank=True, max_length=500, null=True, verbose_name='Descripción')),
                ('descriptionnnn', models.CharField(blank=True, max_length=500, null=True, verbose_name='Descripción')),
                ('is_avaliable', models.BooleanField(default=True)),
            ],
        ),
    ]
