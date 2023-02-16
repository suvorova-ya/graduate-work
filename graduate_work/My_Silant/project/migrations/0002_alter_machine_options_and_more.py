# Generated by Django 4.1.6 on 2023-02-07 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='machine',
            options={'ordering': ('delivery_date',), 'verbose_name': 'Машина', 'verbose_name_plural': 'Машины'},
        ),
        migrations.AlterModelOptions(
            name='maintenance_operation',
            options={'ordering': ('date_maintenance_operation',), 'verbose_name': 'Техническое обслуживание', 'verbose_name_plural': 'Техническое обслуживание'},
        ),
        migrations.AlterModelOptions(
            name='reclamation',
            options={'ordering': ('date',), 'verbose_name': 'Рекламация', 'verbose_name_plural': 'Рекламация'},
        ),
    ]