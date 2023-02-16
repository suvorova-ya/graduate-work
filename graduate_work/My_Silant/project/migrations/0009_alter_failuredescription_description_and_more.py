# Generated by Django 4.1.6 on 2023-02-12 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_alter_maintenance_operation_operation_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='failuredescription',
            name='description',
            field=models.TextField(max_length=600, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='failuredescription',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='modeldriveaxle',
            name='description',
            field=models.TextField(max_length=600, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='modeldriveaxle',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='modelengine',
            name='description',
            field=models.TextField(max_length=600, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='modelengine',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='modelguidingaxle',
            name='description',
            field=models.TextField(max_length=600, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='modelguidingaxle',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='modelmashine',
            name='description',
            field=models.TextField(max_length=600, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='modelmashine',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='modeltransmission',
            name='description',
            field=models.TextField(max_length=600, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='modeltransmission',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='repairingtype',
            name='description',
            field=models.TextField(max_length=600, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='repairingtype',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='type_maintenance_operation',
            name='description',
            field=models.TextField(max_length=600, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='type_maintenance_operation',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Название'),
        ),
    ]