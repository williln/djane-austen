# Generated by Django 2.1.1 on 2018-09-29 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='accomplishment',
            new_name='accomplishments',
        ),
    ]
