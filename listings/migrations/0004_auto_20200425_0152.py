# Generated by Django 2.2.5 on 2020-04-24 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20200425_0149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mobilephone',
            name='messaging',
        ),
        migrations.AlterField(
            model_name='mobilephone',
            name='gpu',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='GPU'),
        ),
        migrations.AlterField(
            model_name='mobilephone',
            name='sensors',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='mobilephone',
            name='usb',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='USB'),
        ),
    ]