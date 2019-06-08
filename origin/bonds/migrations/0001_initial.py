# Generated by Django 2.2.1 on 2019-06-07 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bond',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isin', models.CharField(max_length=30)),
                ('size', models.CharField(max_length=30)),
                ('currency', models.CharField(max_length=30)),
                ('maturity', models.DateField()),
                ('lei', models.CharField(max_length=30)),
            ],
        ),
    ]
