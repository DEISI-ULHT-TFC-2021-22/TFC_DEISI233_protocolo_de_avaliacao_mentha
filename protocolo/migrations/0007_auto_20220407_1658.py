# Generated by Django 3.1.2 on 2022-04-07 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protocolo', '0006_parte_parte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parte',
            name='parte',
            field=models.IntegerField(blank=True),
        ),
    ]