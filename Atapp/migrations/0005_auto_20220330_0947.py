# Generated by Django 3.2.10 on 2022-03-30 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Atapp', '0004_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='firstname',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='book',
            name='lastname',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
