# Generated by Django 5.1.2 on 2024-10-30 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='static/img/special-1.jpg', upload_to='img/'),
        ),
    ]
