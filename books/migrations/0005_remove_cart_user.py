# Generated by Django 5.0.3 on 2024-03-27 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_cart_cartitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
    ]
