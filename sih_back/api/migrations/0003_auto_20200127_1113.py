# Generated by Django 2.2.9 on 2020-01-27 05:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200127_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesslog',
            name='entry_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
