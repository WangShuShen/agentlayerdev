# Generated by Django 4.1.1 on 2023-12-06 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('central_layer_data_mgt', '0002_teacher_delete_role'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]