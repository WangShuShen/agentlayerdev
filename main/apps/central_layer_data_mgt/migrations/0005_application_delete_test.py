# Generated by Django 4.1.1 on 2023-12-06 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('central_layer_data_mgt', '0004_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('application_uid', models.UUIDField(blank=True, primary_key=True, serialize=False, unique=True)),
                ('application_created_time', models.DateTimeField(max_length=255)),
                ('application_description', models.TextField(default='Application description', max_length=255)),
                ('application_name', models.CharField(blank=True, default='Application name', max_length=255)),
            ],
            options={
                'db_table': 'application',
                'managed': True,
            },
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]
