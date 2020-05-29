from django.db import models
from django.core.validators import int_list_validator
from django.contrib.auth.models import User
import os


def image_upload_path(instance, filename):
    return os.path.join(
        'phones',
        instance.name,
        filename
    )

class Brand(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name

class MobilePhone(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('upcoming', 'Upcoming'),

    ]
    CAMERA_CHOICES = [
        ('single', 'Single'),
        ('dual', 'Dual'),
        ('triple', 'Triple'),
        ('triple+', 'Triple+'),
    ]
    CPU_TYPES = [
        ('single', 'Single-core'),
        ('dual', 'Dual-core'),
        ('quad', 'Quad-core'),
        ('hexa', 'Hexa-core'),
        ('octa', 'Octa-core'),
    ]
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, related_name="phones")
    name = models.CharField(max_length=100)
    # Price&Color
    price = models.IntegerField()
    color = models.CharField(max_length=200, blank=True, null=True)
    # Launch
    announced_date = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    released_date = models.CharField(max_length=100, blank=True, null=True)
    # Display
    display_type = models.CharField(max_length=100)
    display_size = models.FloatField(blank=True, null=True)
    display_resolution = models.CharField(max_length=20)
    multitouch = models.BooleanField(default=True)
    # Body
    dimensions = models.CharField(max_length=100, blank=True, null=True)
    weight = models.IntegerField(default=None, null=True, blank=True)
    sim = models.CharField(max_length=50, blank=True, null=True)
    # Memory
    ram = models.CharField(validators=[int_list_validator], max_length=100, null=True, blank=True)
    storage = models.CharField(validators=[int_list_validator], max_length=100, null=True, blank=True)
    is_cardslot_exists = models.BooleanField(verbose_name='Card Slot Exists?', default=True)
    card_slot = models.CharField(max_length=100, blank=True, null=True)
    # Main Camera
    is_mc_exists = models.BooleanField(verbose_name='Main Camera Exists?', default=True)
    mc_type = models.CharField(verbose_name='Main Camera Type', max_length=20, choices=CAMERA_CHOICES, blank=True, null=True)
    mc = models.CharField(verbose_name='Main Camera Description', max_length=100, blank=True, null=True)
    mc_features = models.CharField(verbose_name='Main Camera Features', max_length=200, blank=True, null=True)
    mc_video = models.CharField(verbose_name='Video', max_length=200, blank=True, null=True)
    # Selfie Camera
    is_sc_exists = models.BooleanField(verbose_name='Selfie Camera Exists?', default=True)
    sc_type = models.CharField(verbose_name='Selfie Camera Type', max_length=20, choices=CAMERA_CHOICES, blank=True, null=True)
    sc = models.CharField(verbose_name='Selfie Camera Description', max_length=100, blank=True, null=True)
    sc_features = models.CharField(verbose_name='Selfie Camera Features', max_length=200, blank=True, null=True)
    sc_video = models.CharField(verbose_name='Video', max_length=200, blank=True, null=True)
    # Sound
    loudspeaker = models.BooleanField(default=True)
    headphone_connector = models.BooleanField(default=True, help_text='3.5mm jack')
    # Platform
    os = models.CharField(max_length=50, blank=True, null=True)
    cpu_type = models.CharField(max_length=20, choices=CPU_TYPES)
    cpu = models.CharField(verbose_name='CPU', max_length=100, blank=True, null=True)
    chipset = models.CharField(max_length=100, blank=True, null=True)
    gpu = models.CharField(verbose_name='GPU', max_length=100, blank=True, null=True)
    # Communication
    network = models.CharField(max_length=100, blank=True, null=True)
    wlan = models.BooleanField(verbose_name='WLAN', default=True)
    bluetooth = models.BooleanField(default=True)
    gps = models.BooleanField(verbose_name='GPS', default=True)
    radio = models.BooleanField(default=True)
    nfc = models.BooleanField(verbose_name='NFC', default=False)
    usb = models.CharField(verbose_name='USB', max_length=100, null=True, blank=True)
    # Misc
    is_battery_removable = models.BooleanField(verbose_name='Battery Removable?', default=False)
    battery_type = models.CharField(max_length=20)
    battery_capacity = models.IntegerField()
    sensors = models.CharField(max_length=100, null=True)
    #Photo
    photo_main = models.ImageField(upload_to=image_upload_path)
    photo_1 = models.ImageField(upload_to=image_upload_path, blank=True)
    photo_2 = models.ImageField(upload_to=image_upload_path, blank=True)
    photo_3 = models.ImageField(upload_to=image_upload_path, blank=True)
    photo_4 = models.ImageField(upload_to=image_upload_path, blank=True)
    photo_5 = models.ImageField(upload_to=image_upload_path, blank=True)
    photo_6 = models.ImageField(upload_to=image_upload_path, blank=True)
    # Phone of the week
    is_wkp = models.BooleanField(verbose_name='Is Phone of the week?', default=False)
    description = models.TextField(max_length=5000, blank=True, null=True)

    def __str__(self):
        return self.name

class PhoneLikes(models.Model):
    username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    phone_id = models.ForeignKey(MobilePhone, on_delete=models.CASCADE, related_name="likes")

class PhoneReviews(models.Model):
    username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    phone_id = models.ForeignKey(MobilePhone, on_delete=models.CASCADE, related_name="reviews")

class Comment(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="comments", null=True)
    phone_id = models.ForeignKey(MobilePhone, on_delete=models.CASCADE, related_name="comments", null=True)
    reply_id = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name="replies", null=True, default=None)
    content = models.TextField(default=None, null=True)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.created_date)

class CommentLikes(models.Model):
    username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="likes")
