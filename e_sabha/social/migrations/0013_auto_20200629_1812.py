# Generated by Django 3.0.7 on 2020-06-29 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0012_auto_20200629_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
