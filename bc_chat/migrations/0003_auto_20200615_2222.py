# Generated by Django 2.2.3 on 2020-06-16 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bc_chat', '0002_auto_20200615_2152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='poster_id',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]