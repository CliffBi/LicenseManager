# Generated by Django 4.0.1 on 2022-01-31 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Licenses', '0004_rename_gpl_approved_licenses_gpl_compatible_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='Licenses',
            options={'ordering': ['-license_name']},
        ),
    ]
