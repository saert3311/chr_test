# Generated by Django 4.1.7 on 2023-05-17 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_proyecto_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stations',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='stations',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
