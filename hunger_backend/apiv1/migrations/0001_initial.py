# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='County',
            fields=[
                ('fips', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('median_housing_one', models.FloatField()),
                ('median_housing_three', models.FloatField()),
                ('median_housing_four', models.FloatField()),
                ('meal_supplement_in_dollar', models.FloatField()),
                ('cost_per_meal', models.FloatField()),
                ('monthly_cost_one', models.FloatField()),
                ('monthly_cost_three', models.FloatField()),
                ('monthly_cost_four', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'counties',
            },
        ),
    ]
