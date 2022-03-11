# Generated by Django 3.2.9 on 2021-11-21 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro', '0002_new'),
    ]

    operations = [
        migrations.CreateModel(
            name='deleteitem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adh', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=50)),
                ('qua', models.CharField(max_length=500)),
                ('add1', models.CharField(max_length=500)),
                ('add2', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zip', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='deta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adh', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=50)),
                ('qua', models.CharField(max_length=500)),
                ('add1', models.CharField(max_length=500)),
                ('add2', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zip', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='new',
        ),
    ]