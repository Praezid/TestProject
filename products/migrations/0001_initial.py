# Generated by Django 3.2.2 on 2021-12-18 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
