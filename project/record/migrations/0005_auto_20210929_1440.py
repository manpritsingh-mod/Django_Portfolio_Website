# Generated by Django 3.2.7 on 2021-09-29 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0004_auto_20210929_1051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aut',
            old_name='ps',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='aut',
            old_name='un',
            new_name='username',
        ),
    ]
