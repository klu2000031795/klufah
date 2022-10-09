# Generated by Django 3.2.10 on 2022-04-23 16:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Atapp', '0026_auto_20220423_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='dashuser',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='Dashuser', to=settings.AUTH_USER_MODEL),
        ),
    ]
