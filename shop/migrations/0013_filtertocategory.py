# Generated by Django 2.1.1 on 2018-10-11 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_producttofilter'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilterToCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Category')),
                ('filter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Filter')),
            ],
            options={
                'db_table': 'shop_filter_to_category',
            },
        ),
    ]
