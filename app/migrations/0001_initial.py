# Generated by Django 4.2.7 on 2023-11-23 22:52

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensort', models.FloatField()),
                ('servo_vertical', models.FloatField()),
                ('secury_mode', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='UserEntity',
            fields=[
                ('user', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=128, unique=True, validators=[django.core.validators.EmailValidator()])),
            ],
        ),
    ]
