# Generated by Django 3.0.4 on 2020-03-18 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_user_is_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(max_length=50, null=True),
        ),
    ]