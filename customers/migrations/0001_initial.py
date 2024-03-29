# Generated by Django 4.1.7 on 2023-03-14 08:42

import computedfields.resolver
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=50, unique=True)),
                ('rent_due', models.FloatField()),
                ('rent_paid', models.FloatField(default=0)),
                ('starting_date', models.DateField()),
                ('due_date', models.DateField()),
                ('deposit', models.FloatField(default=0)),
                ('address', models.CharField(max_length=100)),
                ('balance', models.FloatField(editable=False)),
                ('remainig_days', models.IntegerField(editable=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(computedfields.resolver._ComputedFieldsModelBase, models.Model),
        ),
        migrations.CreateModel(
            name='RealState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
            ],
        ),
    ]
