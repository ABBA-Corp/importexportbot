# Generated by Django 4.1.4 on 2022-12-20 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_productcategory_user_company_user_monthly_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='full',
            field=models.BooleanField(default=False),
        ),
    ]
