# Generated by Django 4.0.1 on 2022-02-05 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("along_neva_channels", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="tour",
            name="points",
            field=models.ManyToManyField(to="along_neva_channels.Point"),
        ),
    ]
