# Generated by Django 2.0.3 on 2018-04-28 03:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0004_auto_20180428_0222'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='host',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dash.User'),
        ),
    ]