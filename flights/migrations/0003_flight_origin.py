# Generated by Django 4.2 on 2023-12-08 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_airport'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='origin',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='flights.airport'),
            preserve_default=False,
        ),
    ]
