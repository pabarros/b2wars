# Generated by Django 2.1.7 on 2019-02-24 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planet',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Name'),
        ),
    ]
