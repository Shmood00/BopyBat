# Generated by Django 2.1.7 on 2019-03-14 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pastebin', '0005_auto_20190313_2014'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bopie',
            old_name='is_disabled',
            new_name='disable_bopie',
        ),
        migrations.AlterField(
            model_name='bopie',
            name='content',
            field=models.TextField(),
        ),
    ]
