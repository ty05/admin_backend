# Generated by Django 3.1.7 on 2022-01-09 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cors', '0007_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_ambassador',
            field=models.BooleanField(default=False),
        ),
    ]
