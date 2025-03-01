# Generated by Django 4.1.7 on 2023-06-19 18:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service_app', '0016_alter_mainservice_time_off_alter_mainservice_time_on'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.AlterField(
            model_name='mainservice',
            name='time_off',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 19, 18, 30, 20, 907878, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='mainservice',
            name='time_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 19, 18, 30, 20, 907878, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order_cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='service_app.ordercart')),
                ('sub_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service_app.subservice')),
            ],
        ),
        migrations.AddField(
            model_name='ordercart',
            name='main_service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service_app.mainservice'),
        ),
    ]
