# Generated by Django 4.2.7 on 2023-12-30 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_bank'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Bank',
        ),
    ]
