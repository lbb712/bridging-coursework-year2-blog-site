# Generated by Django 2.2.13 on 2020-08-20 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cveditor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
