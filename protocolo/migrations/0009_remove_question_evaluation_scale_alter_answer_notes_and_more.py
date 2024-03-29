# Generated by Django 4.0.5 on 2022-08-23 22:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protocolo', '0008_possibleanswer_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='evaluation_scale',
        ),
        migrations.AlterField(
            model_name='answer',
            name='notes',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='text_answer',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='area',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='area',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='dimension',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='dimension',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='instrument',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='instrument',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='multiplechoicescheckbox',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='multiplechoicescheckbox',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='part',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='part',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='possibleanswer',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='possibleanswer',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='protocol',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='protocol',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='question',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='instruction',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='question',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9)]),
        ),
        migrations.AlterField(
            model_name='questionimage',
            name='description',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='questionimage',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='section',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='textinputanswer',
            name='text',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
