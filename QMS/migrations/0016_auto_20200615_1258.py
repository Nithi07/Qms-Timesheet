# Generated by Django 3.0 on 2020-06-15 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QMS', '0015_auto_20200615_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditschedule',
            name='schedule_iso_year',
            field=models.CharField(max_length=50, null=True),
        ),
    ]