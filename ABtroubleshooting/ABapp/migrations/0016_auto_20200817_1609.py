# Generated by Django 3.0.3 on 2020-08-17 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ABapp', '0015_auto_20200817_1209'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ab_data',
            old_name='IPCReason',
            new_name='InStock_status',
        ),
        migrations.RenameField(
            model_name='ab_data',
            old_name='Inventory',
            new_name='Ipc_status_reason',
        ),
    ]
