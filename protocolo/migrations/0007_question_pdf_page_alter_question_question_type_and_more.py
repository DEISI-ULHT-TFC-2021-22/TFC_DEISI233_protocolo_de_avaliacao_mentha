# Generated by Django 4.0.5 on 2022-08-12 14:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protocolo', '0006_alter_question_instruction_textinputanswer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='pdf_page',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='question',
            name='quotation_max',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='question',
            name='quotation_min',
            field=models.IntegerField(default=0),
        ),
    ]
