# Generated by Django 2.0.3 on 2018-04-28 03:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0005_result_host'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dash.User'),
        ),
    ]
