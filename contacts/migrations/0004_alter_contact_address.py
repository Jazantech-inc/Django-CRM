# Generated by Django 4.2.1 on 2023-11-23 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_alter_contact_secondary_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
