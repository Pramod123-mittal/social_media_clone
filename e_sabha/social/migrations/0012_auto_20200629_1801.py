# Generated by Django 3.0.7 on 2020-06-29 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0011_auto_20200629_1720'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='desc',
            new_name='msg',
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]