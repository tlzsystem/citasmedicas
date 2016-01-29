# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('citas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='centro',
            name='logo',
            field=models.ImageField(default=datetime.datetime(2016, 1, 28, 2, 29, 9, 777008, tzinfo=utc), upload_to=b'logos'),
            preserve_default=False,
        ),
    ]
