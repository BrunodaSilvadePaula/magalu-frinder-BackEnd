# Generated by Django 2.0.7 on 2018-07-28 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lojas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loja',
            name='cod_filial',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]