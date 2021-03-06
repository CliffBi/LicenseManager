# Generated by Django 4.0.1 on 2022-02-22 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Licenses', '0015_licenses_guarantee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='licenses',
            name='copyright_holder',
        ),
        migrations.AddField(
            model_name='licenses',
            name='active',
            field=models.BooleanField(default=True, help_text='Check'),
        ),
        migrations.AlterField(
            model_name='licenses',
            name='copyleft',
            field=models.BooleanField(default=True, help_text='Is Copyleft a license?'),
        ),
        migrations.AlterField(
            model_name='licenses',
            name='guarantee',
            field=models.BooleanField(blank=True, help_text='Is the license guaranteed?', null=True),
        ),
    ]
