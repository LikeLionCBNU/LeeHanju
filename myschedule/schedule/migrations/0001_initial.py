# Generated by Django 2.1.7 on 2020-07-01 13:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('memo', models.TextField()),
                ('schedule_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('publish_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
