# Generated by Django 3.1.2 on 2020-10-20 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0004_auto_20201020_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='./static/media/trousers/'),
        ),
    ]