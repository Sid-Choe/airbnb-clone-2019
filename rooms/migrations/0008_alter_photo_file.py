# Generated by Django 4.1.1 on 2022-09-14 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0007_alter_room_amenities_alter_room_facility_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.ImageField(blank=True, upload_to='room_photos'),
        ),
    ]
