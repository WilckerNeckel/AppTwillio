# Generated by Django 4.2.6 on 2023-11-07 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ReceiveSms', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Dados_da_msg',
            new_name='SmsInfo',
        ),
    ]
