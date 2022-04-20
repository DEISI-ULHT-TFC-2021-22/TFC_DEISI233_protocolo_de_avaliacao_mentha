# Generated by Django 3.1.2 on 2022-04-08 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('protocolo', '0011_auto_20220407_1720'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('order', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Dimension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('order', models.IntegerField(default=0)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='protocolo.area')),
            ],
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('order', models.IntegerField(default=0)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='protocolo.area')),
            ],
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('order', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Protocol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('order', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('order', models.IntegerField(default=0)),
                ('description', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('order', models.IntegerField(default=0)),
                ('dimension', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='protocolo.dimension')),
            ],
        ),
        migrations.RemoveField(
            model_name='parte',
            name='protocolo',
        ),
        migrations.DeleteModel(
            name='AreasDeAvaliacao',
        ),
        migrations.DeleteModel(
            name='Parte',
        ),
        migrations.DeleteModel(
            name='Protocolo',
        ),
        migrations.AddField(
            model_name='question',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='protocolo.section'),
        ),
        migrations.AddField(
            model_name='part',
            name='protocol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='protocolo.protocol'),
        ),
        migrations.AddField(
            model_name='area',
            name='parts',
            field=models.ManyToManyField(default=None, related_name='areas', to='protocolo.Part'),
        ),
    ]
