# Generated by Django 2.2.13 on 2020-08-26 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cveditor', '0009_auto_20200826_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='phone',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
