# Generated by Django 4.1.1 on 2022-09-13 13:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        auto_created=True,
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "total_value",
                    models.DecimalField(decimal_places=8, default=0, max_digits=20),
                ),
                ("quantity", models.DecimalField(decimal_places=8, max_digits=10)),
                (
                    "exchange",
                    models.CharField(
                        choices=[("buy", "Buy"), ("sell", "Sell")], max_length=50
                    ),
                ),
                ("quotation", models.DecimalField(decimal_places=8, max_digits=20)),
                ("transaction_date_time", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
