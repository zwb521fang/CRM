# Generated by Django 2.0.2 on 2018-05-06 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
