# Generated by Django 4.1.4 on 2023-01-08 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0026_remove_loaderservice_tonnas_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customs',
            name='contact',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]
