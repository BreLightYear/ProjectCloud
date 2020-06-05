# Generated by Django 2.2.4 on 2019-09-03 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_person_created_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='country',
            field=models.CharField(choices=[('0', ' '), ('1', 'Brasil')], default=0, max_length=50, verbose_name='Pais'),
        ),
        migrations.AlterField(
            model_name='person',
            name='region',
            field=models.CharField(choices=[('0', ' '), ('1', 'Sao Paulo'), ('2', 'Rio de Janeiro')], default=0, max_length=50, verbose_name='Região'),
        ),
    ]