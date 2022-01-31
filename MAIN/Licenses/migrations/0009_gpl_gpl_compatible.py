# Generated by Django 4.0.1 on 2022-01-31 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Licenses', '0008_gpl'),
    ]

    operations = [
        migrations.AddField(
            model_name='gpl',
            name='GPL_compatible',
            field=models.BooleanField(default=True, help_text='Is it compatible with GPL?'),
            preserve_default=False,
        ),
    ]