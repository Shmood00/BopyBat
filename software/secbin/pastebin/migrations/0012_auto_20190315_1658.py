# Generated by Django 2.1.7 on 2019-03-15 21:58

import datetime
from django.db import migrations, models
import pastebin.models
import pastebin.validators


class Migration(migrations.Migration):

    dependencies = [
        ('pastebin', '0011_auto_20190314_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bopie',
            name='date_expiry',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 3, 17, 16, 58, 25, 968439), null=True, verbose_name='Expiry Date'),
        ),
        migrations.AlterField(
            model_name='bopie',
            name='postUpload',
            field=models.FileField(blank=True, null=True, upload_to=pastebin.models.unique_file_name, validators=[pastebin.validators.validate_file_size_type], verbose_name='Upload Post'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profilePic',
            field=models.ImageField(default='default.png', upload_to=pastebin.models.pic_file_path, validators=[pastebin.validators.validate_file_size_type], verbose_name='Profile Picture'),
        ),
    ]
