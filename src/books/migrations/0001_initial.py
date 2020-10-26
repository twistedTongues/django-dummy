# Generated by Django 3.1.2 on 2020-10-26 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('references', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('books', models.CharField(max_length=1000, verbose_name='Title of the Book')),
                ('description', models.TextField(blank=True, null=True, verbose_name='About Book')),
                ('photo_cover', models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Cover of the book')),
                ('price', models.DecimalField(decimal_places=3, default=0, max_digits=10, verbose_name='Price in USA dollars')),
                ('date_of_establishment', models.DateTimeField(blank=True, null=True, verbose_name='Date of establishment')),
                ('amount_of_pages', models.PositiveIntegerField(default=0, verbose_name='Amount of Pages')),
                ('binding', models.CharField(choices=[('1', 'Paperback'), ('2', 'Hardcover'), ('3', 'Large Print'), ('4', 'Audible Audiobook'), ('5', 'Printed Access Code'), ('6', 'Loose Leaf'), ('7', 'Audio CD'), ('8', 'Board Book')], default=1, max_length=100, verbose_name='Binding')),
                ('format', models.CharField(choices=[('1', '70×90/8'), ('2', '70×90/16'), ('3', '70×90/32'), ('4', '70×108/32'), ('5', '60×90/16'), ('6', '60×90/32'), ('7', '84×108/32')], default=1, max_length=100, verbose_name='Format')),
                ('isbn_id', models.CharField(default='', max_length=20, verbose_name='ISBN')),
                ('book_weight', models.PositiveIntegerField(default=0, verbose_name="Book's weight in Weight (g)")),
                ('age_limit', models.CharField(choices=[('1', '3+'), ('2', '6+'), ('3', '12+'), ('4', '14+'), ('5', '16 +'), ('6', '18+'), ('7', '21+')], default=1, max_length=4, verbose_name='Age limit')),
                ('conditions', models.CharField(choices=[('1', 'New'), ('2', 'Used'), ('3', 'Collectible')], default=1, max_length=4, verbose_name='conditions')),
                ('number_of_books', models.PositiveIntegerField(default=0, verbose_name='Number of Books Available')),
                ('book_availability', models.CharField(choices=[('yes', 'AVAILABLE'), ('no', 'NOT AVAILABLE')], default='no', max_length=20, verbose_name='Book Status')),
                ('rating', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default=0, max_length=5, verbose_name='Rating of the book')),
                ('book_adding_date', models.DateField(auto_now_add=True, verbose_name='Publishing date in shop')),
                ('book_updating_date', models.DateTimeField(auto_now=True, verbose_name='Date of updating Book')),
                ('author', models.ManyToManyField(related_name='book', to='references.Author', verbose_name='Author')),
                ('genres', models.ManyToManyField(related_name='book', to='references.Genre', verbose_name='Genre')),
                ('languages', models.ManyToManyField(to='references.Language', verbose_name='Language')),
                ('pub_house', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='book', to='references.publishinghouse')),
                ('series', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='book', to='references.bookseries', verbose_name='Title of the Serie')),
            ],
        ),
    ]