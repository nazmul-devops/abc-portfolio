# Generated by Django 4.2.4 on 2023-08-27 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Posts",
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
                ("post_title", models.CharField(max_length=100)),
                ("post_des", models.TextField()),
                ("post_image", models.FileField(upload_to="")),
            ],
        ),
    ]