# Generated by Django 3.0.7 on 2020-06-25 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0005_auto_20200625_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mypost',
            name='uploaded_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='social.MyProfile'),
        ),
    ]