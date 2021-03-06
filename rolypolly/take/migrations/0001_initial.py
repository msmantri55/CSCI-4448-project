# Generated by Django 2.0.3 on 2018-04-12 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dash', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField()),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dash.Answer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dash.Question')),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dash.Result')),
            ],
        ),
    ]
