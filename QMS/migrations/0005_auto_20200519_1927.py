# Generated by Django 3.0 on 2020-05-19 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QMS', '0004_auto_20200519_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audit_comments',
            name='auditor_comments',
            field=models.TextField(blank=True, null=True),
        ),
    ]
