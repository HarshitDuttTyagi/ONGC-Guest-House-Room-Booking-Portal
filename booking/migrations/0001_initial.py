# Generated by Django 2.1.2 on 2018-10-09 07:19

import booking.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtendedUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=11, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=booking.models.get_image_path)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='GuestHouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.IntegerField()),
                ('room_type', models.CharField(choices=[('Single AC', 'Single AC'), ('Double AC', 'Double AC'), ('Single NON AC', 'Single NON AC'), ('Double NON AC', 'Double NON AC')], max_length=20)),
                ('guesthouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.GuestHouse')),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('no_people', models.IntegerField(blank=True, null=True)),
                ('room_no', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='booking.Rooms')),
                ('user_booked', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]