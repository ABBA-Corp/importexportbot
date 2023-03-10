# Generated by Django 4.1.4 on 2023-01-08 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0025_alter_user_monthly'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loaderservice',
            name='tonnas',
        ),
        migrations.RemoveField(
            model_name='loaderservice',
            name='type_en',
        ),
        migrations.RemoveField(
            model_name='loaderservice',
            name='type_ru',
        ),
        migrations.RemoveField(
            model_name='loaderservice',
            name='type_uz',
        ),
        migrations.AddField(
            model_name='loaderservice',
            name='name_en',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='loaderservice',
            name='name_ru',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='loaderservice',
            name='name_uz',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='loaderservice',
            name='persons',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
