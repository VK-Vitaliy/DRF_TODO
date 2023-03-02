# Generated by Django 3.2.8 on 2023-02-28 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, verbose_name='username')),
                ('first_name', models.CharField(max_length=64, verbose_name='first name')),
                ('last_name', models.CharField(max_length=64, verbose_name='last_name')),
                ('email', models.CharField(max_length=256, unique=True, verbose_name='email address')),
            ],
        ),
    ]
