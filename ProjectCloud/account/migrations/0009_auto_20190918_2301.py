# Generated by Django 2.2.4 on 2019-09-18 23:01

import account.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20190918_2239'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=False, max_length=50, verbose_name='Ativo')),
                ('name', models.CharField(blank=True, help_text='Nome da organização', max_length=50)),
                ('cnpj', models.CharField(max_length=50, unique=True, validators=[account.validators.validate_CNPJ], verbose_name='CNPJ')),
                ('adress', models.CharField(max_length=50, verbose_name='Endereço da organização')),
                ('region', models.CharField(choices=[('0', ' '), ('1', 'Sao Paulo'), ('2', 'Rio de Janeiro')], default=0, max_length=50, verbose_name='Região')),
            ],
        ),
        migrations.AlterField(
            model_name='person',
            name='adress',
            field=models.CharField(help_text='Endereço', max_length=50, verbose_name='Endereço'),
        ),
    ]