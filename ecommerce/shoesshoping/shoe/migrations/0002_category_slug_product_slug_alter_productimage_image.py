# Generated by Django 4.2.3 on 2023-07-29 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product'),
        ),
    ]
