# Generated by Django 4.2.5 on 2023-09-13 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hbalances', '0002_hbalances_status_alter_hbalances_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hbalances',
            name='date',
            field=models.DateField(max_length=30),
        ),
    ]
