# Generated by Django 5.0.6 on 2024-06-15 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='deliver',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
