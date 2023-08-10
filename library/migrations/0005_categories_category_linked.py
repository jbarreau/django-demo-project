# Generated by Django 4.2 on 2023-05-24 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("library", "0004_categorieslinked_alter_categories_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="categories",
            name="category_linked",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="library.categorieslinked",
            ),
        ),
    ]