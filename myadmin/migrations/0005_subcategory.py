# Generated by Django 4.2.2 on 2023-08-19 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0004_delete_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('subcatid', models.AutoField(primary_key=True, serialize=False)),
                ('catname', models.CharField(max_length=50)),
                ('subcatname', models.CharField(max_length=50, unique=True)),
                ('subcaticonname', models.CharField(max_length=100)),
            ],
        ),
    ]
