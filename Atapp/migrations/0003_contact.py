# Generated by Django 4.0.1 on 2022-02-26 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Atapp', '0002_alter_book_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
    ]
