# Generated by Django 4.2.4 on 2023-08-27 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Posts",
            new_name="Post",
        ),
    ]
