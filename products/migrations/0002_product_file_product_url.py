# Generated by Django 5.1 on 2024-12-15 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='product_files/'),
        ),
        migrations.AddField(
            model_name='product',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
