# Generated by Django 4.1.4 on 2023-01-06 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0016_loaderequipment_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='TnVed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kod', models.CharField(blank=True, max_length=500, null=True)),
                ('description_uz', models.TextField(blank=True, max_length=5000, null=True)),
                ('description_en', models.TextField(blank=True, max_length=5000, null=True)),
                ('description_ru', models.TextField(blank=True, max_length=5000, null=True)),
            ],
        ),
    ]
