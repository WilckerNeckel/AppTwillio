# Generated by Django 4.2.6 on 2023-11-07 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dados_da_msg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=50)),
                ('sender', models.CharField(max_length=20)),
                ('recipient', models.CharField(max_length=20)),
            ],
        ),
    ]