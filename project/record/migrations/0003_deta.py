# Generated by Django 3.2.7 on 2021-09-29 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0002_alter_aut_pho'),
    ]

    operations = [
        migrations.CreateModel(
            name='deta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('qua', models.CharField(max_length=50)),
                ('add1', models.CharField(max_length=50)),
                ('add2', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zip', models.CharField(max_length=50)),
            ],
        ),
    ]
