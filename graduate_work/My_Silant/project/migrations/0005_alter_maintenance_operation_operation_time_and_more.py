# Generated by Django 4.1.6 on 2023-02-11 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_alter_machine_options_machine_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenance_operation',
            name='operation_time',
            field=models.IntegerField(verbose_name='Наработка, м/час'),
        ),
        migrations.AlterField(
            model_name='reclamation',
            name='operation_time',
            field=models.IntegerField(verbose_name='Наработка, м/час'),
        ),
    ]
