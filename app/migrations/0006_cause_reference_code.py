# Generated by Django 3.1.2 on 2020-10-30 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20201016_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='cause',
            name='reference_code',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
