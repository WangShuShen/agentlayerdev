# Generated by Django 4.1.1 on 2023-12-05 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('central_layer_data_mgt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]
