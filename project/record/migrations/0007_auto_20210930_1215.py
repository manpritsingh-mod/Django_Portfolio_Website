# Generated by Django 3.2.7 on 2021-09-30 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0006_deta_adh'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aut',
            name='id',
        ),
        migrations.RemoveField(
            model_name='deta',
            name='id',
        ),
        migrations.AlterField(
            model_name='aut',
            name='pho',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='deta',
            name='adh',
            field=models.CharField(max_length=500, primary_key=True, serialize=False),
        ),
    ]