# Generated by Django 2.0.7 on 2018-07-28 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_produto', models.CharField(max_length=15, unique=True)),
                ('descricao', models.TextField()),
                ('valor_venda', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
