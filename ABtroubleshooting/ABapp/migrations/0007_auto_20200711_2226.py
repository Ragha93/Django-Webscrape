# Generated by Django 3.0.3 on 2020-07-11 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ABapp', '0006_ab_data_blacklist_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='ab_template',
            name='taskid',
            field=models.IntegerField(default='1993'),
        ),
        migrations.AddField(
            model_name='ab_troubleshooting',
            name='taskid',
            field=models.IntegerField(default='1993'),
        ),
    ]