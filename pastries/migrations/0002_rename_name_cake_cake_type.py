# Generated by Django 4.2.2 on 2023-06-22 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pastries', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cake',
            old_name='name',
            new_name='cake_type',
        ),
    ]
