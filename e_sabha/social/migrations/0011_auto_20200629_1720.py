# Generated by Django 3.0.7 on 2020-06-29 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0010_auto_20200629_1645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='msg',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='pno',
        ),
        migrations.AddField(
            model_name='contact',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='desc',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
