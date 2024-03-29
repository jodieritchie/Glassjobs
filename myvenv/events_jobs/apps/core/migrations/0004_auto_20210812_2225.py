# Generated by Django 3.2.6 on 2021-08-13 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_application'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='company_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='company_country',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='company_name',
            field=models.CharField(default='Default name', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='company_place',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='company_size',
            field=models.CharField(choices=[('size_1-20', '1-20'), ('size_21-100', '21-100'), ('size_101-999', '101-999'), ('size_1000+', '1000+')], default='size_1-20', max_length=20),
        ),
        migrations.AddField(
            model_name='job',
            name='company_zipcode',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
