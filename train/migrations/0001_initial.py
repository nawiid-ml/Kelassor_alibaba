# Generated by Django 4.2 on 2023-12-15 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Train_Name', models.CharField(max_length=250)),
                ('Origin', models.CharField(max_length=200)),
                ('Destination', models.CharField(max_length=250)),
                ('Date_Of_Departure', models.DateField()),
                ('Return_Of_Departure', models.DateField()),
            ],
        ),
    ]
