# Generated by Django 2.1.7 on 2019-03-14 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pastebin', '0006_auto_20190313_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='bopie',
            name='make_private',
            field=models.BooleanField(default=False),
        ),
    ]
