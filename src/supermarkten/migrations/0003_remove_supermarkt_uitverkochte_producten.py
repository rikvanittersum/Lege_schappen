# Generated by Django 3.0.9 on 2020-09-03 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supermarkten', '0002_uitverkochte_producten'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supermarkt',
            name='uitverkochte_producten',
        ),
    ]