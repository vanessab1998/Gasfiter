# Generated by Django 4.0.3 on 2024-04-09 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=60)),
                ('email_contact', models.EmailField(max_length=100)),
                ('subject_contact', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=12)),
                ('message_contact', models.CharField(max_length=500)),
            ],
        ),
    ]
