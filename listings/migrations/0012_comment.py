# Generated by Django 2.2.5 on 2020-05-20 00:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('listings', '0011_mobilephone_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='listings.MobilePhone')),
                ('reply_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='listings.Comment')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]