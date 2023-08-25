# Generated by Django 4.2.2 on 2023-07-26 12:33

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Properties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('ptype', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('area', models.IntegerField()),
                ('bed', models.IntegerField()),
                ('bath', models.IntegerField()),
                ('garage', models.IntegerField()),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='post')),
                ('price', models.FloatField()),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('agent_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
