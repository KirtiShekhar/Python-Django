# Generated by Django 4.0.6 on 2022-07-22 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaDeliveryApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerId', models.CharField(max_length=10)),
                ('contactNumber', models.CharField(max_length=10)),
                ('emailAddress', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='pizzamodel',
            name='pizzaName',
            field=models.CharField(max_length=50),
        ),
    ]
