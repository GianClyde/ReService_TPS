# Generated by Django 4.1.7 on 2023-04-09 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student_registration", "0004_routes_included_route"),
    ]

    operations = [
        migrations.AddField(
            model_name="driverprofile",
            name="assigned_route",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name="Routes",
        ),
    ]
