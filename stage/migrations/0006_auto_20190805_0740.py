# Generated by Django 2.2.4 on 2019-08-05 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stage', '0005_app_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='timestamp',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
