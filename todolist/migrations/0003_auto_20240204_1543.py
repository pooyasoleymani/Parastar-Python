# Generated by Django 3.1.3 on 2024-02-04 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_servicerequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
