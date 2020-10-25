# Generated by Django 3.1.2 on 2020-10-25 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0002_auto_20201024_2325'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublishingHouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pubhouse', models.CharField(max_length=40, verbose_name='Publishing House')),
                ('otherbooks', models.TextField(blank=True, max_length=500, null=True, verbose_name='Other books of this house')),
            ],
        ),
        migrations.DeleteModel(
            name='Condition',
        ),
        migrations.DeleteModel(
            name='Format',
        ),
    ]
