# Generated by Django 4.2.3 on 2023-10-29 14:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0005_alter_news_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="created_at",
            field=models.DateField(),
        ),
    ]