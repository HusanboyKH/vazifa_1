# Generated by Django 4.2.2 on 2023-07-03 04:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=65)),
                ('fname', models.CharField(default='', max_length=65)),
                ('date_of_birth', models.DateField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'author',
            },
        ),
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('page', models.PositiveIntegerField(default=1)),
                ('price', models.PositiveIntegerField(default=1)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.authormodel')),
            ],
            options={
                'db_table': 'book',
            },
        ),
    ]