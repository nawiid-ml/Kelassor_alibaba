# Generated by Django 4.2 on 2023-12-15 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0002_alter_train_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='train',
            name='Origin',
        ),
    ]
