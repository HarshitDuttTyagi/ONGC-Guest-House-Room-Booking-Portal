# Generated by Django 2.1.1 on 2018-10-17 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_auto_20181017_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='room_type',
            field=models.CharField(blank=True, choices=[('Single-AC', 'Single-AC'), ('Double-AC', 'Double-AC'), ('Single-NON-AC', 'Single NON-AC'), ('Double-NON-AC', 'Double-NON-AC')], max_length=20, null=True),
        ),
    ]
