# Generated by Django 2.1.7 on 2019-03-14 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pastebin', '0007_bopie_make_private'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bopie',
            name='make_private',
        ),
    ]
