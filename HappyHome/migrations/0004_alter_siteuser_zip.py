# Generated by Django 4.1.7 on 2023-04-13 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HappyHome', '0003_rename_user_siteuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteuser',
            name='zip',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
