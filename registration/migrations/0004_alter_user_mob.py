# Generated by Django 3.2.4 on 2021-06-11 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_alter_user_mob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mob',
            field=models.CharField(max_length=10),
        ),
    ]
