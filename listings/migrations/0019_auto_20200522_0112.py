# Generated by Django 2.2.5 on 2020-05-21 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0018_auto_20200521_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobilephone',
            name='description',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
    ]
