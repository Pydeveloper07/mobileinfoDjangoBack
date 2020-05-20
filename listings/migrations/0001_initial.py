# Generated by Django 2.2.5 on 2020-04-24 16:19

from django.db import migrations, models
import listings.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MobilePhone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('color', models.CharField(blank=True, max_length=200, null=True)),
                ('announced_date', models.DateField()),
                ('status', models.CharField(choices=[('available', 'Available'), ('upcoming', 'Upcoming')], max_length=50)),
                ('released_date', models.DateField(blank=True, null=True)),
                ('display_type', models.CharField(max_length=100)),
                ('display_size', models.FloatField(blank=True, null=True)),
                ('display_resolution', models.CharField(max_length=20)),
                ('multitouch', models.BooleanField(default=True)),
                ('dimensions', models.CharField(blank=True, max_length=100, null=True)),
                ('weight', models.IntegerField()),
                ('sim', models.CharField(blank=True, max_length=50, null=True)),
                ('ram', models.IntegerField(blank=True, null=True)),
                ('storage', models.IntegerField(blank=True, null=True)),
                ('is_cardslot_exists', models.BooleanField(default=True, verbose_name='Card Slot Exists?')),
                ('card_slot', models.CharField(blank=True, max_length=100, null=True)),
                ('is_mc_exists', models.BooleanField(default=True, verbose_name='Main Camera Exists?')),
                ('mc_type', models.CharField(blank=True, choices=[('single', 'Single'), ('double', 'Double'), ('triple', 'Triple'), ('triple+', 'Triple+')], max_length=20, null=True, verbose_name='Main Camera Type')),
                ('mc', models.CharField(blank=True, max_length=100, null=True, verbose_name='Main Camera Description')),
                ('mc_features', models.CharField(blank=True, max_length=200, null=True, verbose_name='Main Camera Features')),
                ('mc_video', models.CharField(blank=True, max_length=200, null=True, verbose_name='Video')),
                ('is_sc_exists', models.BooleanField(default=True, verbose_name='Selfie Camera Exists?')),
                ('sc_type', models.CharField(blank=True, choices=[('single', 'Single'), ('double', 'Double'), ('triple', 'Triple'), ('triple+', 'Triple+')], max_length=20, null=True, verbose_name='Selfie Camera Type')),
                ('sc', models.CharField(blank=True, max_length=100, null=True, verbose_name='Selfie Camera Description')),
                ('sc_features', models.CharField(blank=True, max_length=200, null=True, verbose_name='Selfie Camera Features')),
                ('sc_video', models.CharField(blank=True, max_length=200, null=True, verbose_name='Video')),
                ('loudspeaker', models.BooleanField(default=True)),
                ('headphone_connector', models.BooleanField(default=True, help_text='3.5mm jack')),
                ('os', models.CharField(blank=True, max_length=50, null=True)),
                ('cpu_type', models.CharField(choices=[('single', 'Single-core'), ('double', 'Double-core'), ('quad', 'Quad-core'), ('hexa', 'Hexa-core'), ('octa', 'Octa-core')], max_length=20)),
                ('cpu', models.CharField(blank=True, max_length=100, null=True, verbose_name='CPU details')),
                ('chipset', models.CharField(blank=True, max_length=100, null=True)),
                ('network', models.CharField(blank=True, max_length=100, null=True)),
                ('wlan', models.BooleanField(default=True, verbose_name='WLAN')),
                ('bluetooth', models.BooleanField(default=True)),
                ('gps', models.BooleanField(default=True, verbose_name='GPS')),
                ('radio', models.BooleanField(default=True)),
                ('usb', models.BooleanField(default=True, verbose_name='USB')),
                ('is_battery_removable', models.BooleanField(default=False, verbose_name='Battery Removable?')),
                ('battery_type', models.CharField(max_length=20)),
                ('battery_capacity', models.IntegerField()),
                ('sensors', models.BooleanField(default=True)),
                ('messaging', models.BooleanField(default=True)),
                ('photo_main', models.ImageField(upload_to=listings.models.image_upload_path)),
                ('photo_1', models.ImageField(blank=True, upload_to=listings.models.image_upload_path)),
                ('photo_2', models.ImageField(blank=True, upload_to=listings.models.image_upload_path)),
                ('photo_3', models.ImageField(blank=True, upload_to=listings.models.image_upload_path)),
                ('photo_4', models.ImageField(blank=True, upload_to=listings.models.image_upload_path)),
                ('photo_5', models.ImageField(blank=True, upload_to=listings.models.image_upload_path)),
                ('photo_6', models.ImageField(blank=True, upload_to=listings.models.image_upload_path)),
            ],
        ),
    ]
