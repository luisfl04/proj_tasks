# Generated by Django 5.0 on 2024-02-27 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_dadosregistro_delete_dados'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dadosregistro',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
