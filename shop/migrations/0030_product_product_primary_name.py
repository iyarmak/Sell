# Generated by Django 2.1.1 on 2018-12-03 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0029_auto_20181201_0733'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_primary_name',
            field=models.CharField(default=None, max_length=500),
        ),
    ]
