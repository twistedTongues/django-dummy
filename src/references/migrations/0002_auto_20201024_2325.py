# Generated by Django 3.1.2 on 2020-10-24 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='format',
            name='formats',
            field=models.CharField(max_length=40, verbose_name='Format'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='genres',
            field=models.CharField(max_length=40, verbose_name='Genre'),
        ),
    ]
