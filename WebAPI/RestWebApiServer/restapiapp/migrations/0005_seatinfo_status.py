# Generated by Django 2.2.5 on 2020-02-07 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapiapp', '0004_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='seatinfo',
            name='status',
            field=models.CharField(choices=[('status_attend', 'Attend'), ('status_absent', 'Absent'), ('status_free', 'Free')], default='status_seat', max_length=50),
        ),
    ]
