# Generated by Django 2.1.5 on 2024-03-14 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20240314_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='Image',
            field=models.ImageField(blank=True, upload_to='profile_images/'),
        ),
    ]
