# Generated by Django 2.2.13 on 2020-08-25 10:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cveditor', '0005_auto_20200824_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='cv',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]