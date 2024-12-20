# Generated by Django 5.1.2 on 2024-11-12 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adopt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('nasc', models.CharField(max_length=30)),
                ('cep', models.CharField(max_length=30)),
                ('bairro', models.CharField(max_length=30)),
                ('endereço', models.CharField(max_length=30)),
                ('profissao', models.CharField(max_length=30)),
                ('dog_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('cpf', models.CharField(max_length=30)),
                ('cep', models.CharField(max_length=30)),
                ('bairro', models.CharField(max_length=30)),
                ('endereço', models.CharField(max_length=30)),
                ('dog_name', models.CharField(max_length=30)),
                ('valor_mensal', models.CharField(max_length=30)),
                ('recebimento', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profissao', models.CharField(max_length=30)),
                ('empresa', models.CharField(max_length=30)),
                ('cargo', models.CharField(max_length=30)),
                ('habilitação', models.CharField(max_length=30)),
                ('dirige', models.CharField(max_length=30)),
                ('possui_carro', models.CharField(max_length=30)),
                ('cargo_voluntario', models.CharField(max_length=30)),
                ('nome', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('nasc', models.CharField(max_length=30)),
                ('whats', models.CharField(max_length=30)),
                ('cep', models.CharField(max_length=30)),
                ('bairro', models.CharField(max_length=30)),
                ('endereço', models.CharField(max_length=30)),
            ],
        ),
    ]
