# Generated by Django 4.2.4 on 2023-08-22 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='n_id',
            new_name='nid',
        ),
    ]
