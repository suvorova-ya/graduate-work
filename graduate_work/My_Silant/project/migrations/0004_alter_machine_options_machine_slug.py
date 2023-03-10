# Generated by Django 4.1.6 on 2023-02-09 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_reclamation_services_company'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='machine',
            options={'ordering': ('-delivery_date',), 'verbose_name': 'Машина', 'verbose_name_plural': 'Машины'},
        ),
        migrations.AddField(
            model_name='machine',
            name='slug',
            field=models.SlugField(max_length=250, null=True, unique=True, verbose_name='URL'),
        ),
    ]
