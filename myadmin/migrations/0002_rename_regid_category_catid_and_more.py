# Generated by Django 4.2.2 on 2023-08-19 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='regid',
            new_name='catid',
        ),
        migrations.AlterField(
            model_name='category',
            name='caticonname',
            field=models.CharField(max_length=100),
        ),
    ]
