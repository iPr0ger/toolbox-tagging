# Generated by Django 3.1.7 on 2021-10-27 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_auto_20211027_0958'),
        ('tagging', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taggingresource',
            name='sensitive_data',
            field=models.ManyToManyField(to='categories.SensitiveData'),
        ),
    ]
