# Generated by Django 4.2.1 on 2023-06-14 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("main_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="MainService",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name_service", models.CharField(max_length=100)),
                ("description_service", models.CharField(max_length=1000)),
                ("time_on", models.DateTimeField(auto_now_add=True)),
                ("time_off", models.DateTimeField()),
                (
                    "image",
                    models.ImageField(
                        default="images/default.jpg", upload_to="images/"
                    ),
                ),
                (
                    "hotel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main_app.hotel"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SubService",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name_service", models.CharField(max_length=100)),
                ("catogory", models.CharField(max_length=100)),
                ("price", models.IntegerField()),
                ("delivery_time", models.DateTimeField()),
                (
                    "image",
                    models.ImageField(
                        default="images/default.jpg", upload_to="images/"
                    ),
                ),
                (
                    "main_service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="service_app.mainservice",
                    ),
                ),
            ],
        ),
    ]
