# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KeyCombo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shift', models.BooleanField(default=False)),
                ('alt', models.BooleanField(default=False)),
                ('ctrl', models.BooleanField(default=False)),
                ('meta', models.BooleanField(default=False)),
                ('keychar', models.CharField(max_length=10)),
                ('meaning', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
