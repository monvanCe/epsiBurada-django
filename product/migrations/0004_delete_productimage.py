# Generated by Django 5.1.1 on 2024-10-04 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_rename_image_productimage_images'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]
