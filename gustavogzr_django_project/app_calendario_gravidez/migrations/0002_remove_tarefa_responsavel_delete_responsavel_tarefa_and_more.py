# Generated by Django 4.2.6 on 2023-10-06 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_calendario_gravidez', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarefa',
            name='responsavel',
        ),
        migrations.DeleteModel(
            name='responsavel_tarefa',
        ),
        migrations.DeleteModel(
            name='tarefa',
        ),
    ]