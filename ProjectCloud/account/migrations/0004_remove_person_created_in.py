# Generated by Django 2.2.4 on 2019-09-02 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20190901_0412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='created_in',
        ),
    ]