# Generated by Django 5.0 on 2024-02-29 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0007_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dadoscard',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
