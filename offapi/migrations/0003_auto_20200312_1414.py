# Generated by Django 3.0.4 on 2020-03-12 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offapi', '0002_auto_20200310_0659'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='category_id',
        ),
    ]