# Generated by Django 3.1.7 on 2021-05-05 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0005_auto_20210505_0934'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resource',
            old_name='resource_type',
            new_name='type_of_resource',
        ),
    ]
