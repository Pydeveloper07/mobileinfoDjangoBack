# Generated by Django 2.2.5 on 2020-04-24 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20200425_0130'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobilephone',
            name='gpu',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='GPU'),
        ),
        migrations.AddField(
            model_name='mobilephone',
            name='nfc',
            field=models.BooleanField(default=False, verbose_name='NFC'),
        ),
        migrations.AlterField(
            model_name='mobilephone',
            name='cpu',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='CPU'),
        ),
        migrations.AlterField(
            model_name='mobilephone',
            name='sensors',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='mobilephone',
            name='usb',
            field=models.CharField(max_length=100, verbose_name='USB'),
        ),
    ]