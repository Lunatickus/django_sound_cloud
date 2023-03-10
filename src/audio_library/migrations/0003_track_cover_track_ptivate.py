# Generated by Django 4.1.2 on 2022-10-18 10:05

import django.core.validators
from django.db import migrations, models
import src.base.services


class Migration(migrations.Migration):

    dependencies = [
        ('audio_library', '0002_rename_crate_at_track_create_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to=src.base.services.get_path_upload_cover_track, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg']), src.base.services.validate_size_image]),
        ),
        migrations.AddField(
            model_name='track',
            name='ptivate',
            field=models.BooleanField(default=False),
        ),
    ]
