# Generated by Django 4.0.6 on 2022-07-25 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortfolioWebsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='statics/img/'),
        ),
    ]
