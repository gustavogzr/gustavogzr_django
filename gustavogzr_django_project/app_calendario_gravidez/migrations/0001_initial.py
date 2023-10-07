# Generated by Django 4.2.6 on 2023-10-06 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='responsavel_tarefa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='tarefa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=1000)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_conclusao_prevista', models.DateTimeField()),
                ('responsavel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_calendario_gravidez.responsavel_tarefa')),
            ],
        ),
    ]
