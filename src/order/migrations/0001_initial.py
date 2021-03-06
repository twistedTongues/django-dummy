# Generated by Django 3.1.2 on 2020-12-02 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Comment about order')),
                ('type_of_payment', models.CharField(default=1, max_length=20, verbose_name='Type of payment')),
                ('date_add', models.DateTimeField(auto_now_add=True, verbose_name='Adding date')),
                ('date_last_change', models.DateTimeField(auto_now=True, verbose_name='Last change date')),
                ('cart', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='order', to='cart.cart')),
            ],
            options={
                'verbose_name': 'Order',
            },
        ),
    ]
