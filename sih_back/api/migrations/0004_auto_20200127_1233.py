# Generated by Django 2.2.9 on 2020-01-27 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200127_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesslog',
            name='entry_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]