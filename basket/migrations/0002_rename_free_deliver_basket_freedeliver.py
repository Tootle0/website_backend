# Generated by Django 4.2.5 on 2024-01-10 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basket',
            old_name='free_deliver',
            new_name='freeDeliver',
        ),
    ]
