# Generated by Django 4.0.1 on 2022-01-27 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Licenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_name', models.CharField(max_length=30)),
                ('copyright_holder', models.CharField(max_length=30)),
                ('product_name', models.CharField(max_length=30)),
                ('guarantees', models.CharField(max_length=30)),
            ],
        ),
    ]
