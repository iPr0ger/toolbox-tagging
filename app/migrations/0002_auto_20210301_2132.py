# Generated by Django 3.1.7 on 2021-03-01 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='country_grouping',
        ),
        migrations.AddField(
            model_name='resource',
            name='country_grouping',
            field=models.ManyToManyField(default=1, to='app.CountryGrouping'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='data_type_focus',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.datatypefocus'),
        ),
        migrations.RemoveField(
            model_name='resource',
            name='global_scope',
        ),
        migrations.AddField(
            model_name='resource',
            name='global_scope',
            field=models.ManyToManyField(default=1, to='app.GlobalScope'),
        ),
        migrations.RemoveField(
            model_name='resource',
            name='perspective',
        ),
        migrations.AddField(
            model_name='resource',
            name='perspective',
            field=models.ManyToManyField(to='app.Perspective'),
        ),
        migrations.RemoveField(
            model_name='resource',
            name='research_field',
        ),
        migrations.AddField(
            model_name='resource',
            name='research_field',
            field=models.ManyToManyField(to='app.ResearchField'),
        ),
        migrations.RemoveField(
            model_name='resource',
            name='resource_type',
        ),
        migrations.AddField(
            model_name='resource',
            name='resource_type',
            field=models.ManyToManyField(to='app.ResourceType'),
        ),
        migrations.RemoveField(
            model_name='resource',
            name='specific_topic',
        ),
        migrations.AddField(
            model_name='resource',
            name='specific_topic',
            field=models.ManyToManyField(to='app.SpecificTopic'),
        ),
        migrations.RemoveField(
            model_name='resource',
            name='tags',
        ),
        migrations.AddField(
            model_name='resource',
            name='tags',
            field=models.ManyToManyField(to='app.Tag'),
        ),
    ]
