# Generated by Django 3.1.2 on 2022-04-07 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('protocolo', '0003_auto_20220407_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parte',
            name='descricao',
            field=models.CharField(blank=True, max_length=280),
        ),
        migrations.AlterField(
            model_name='parte',
            name='protocolo',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='partes', to='protocolo.protocolo'),
        ),
        migrations.AlterField(
            model_name='protocolo',
            name='descricao',
            field=models.CharField(blank=True, max_length=280),
        ),
    ]
