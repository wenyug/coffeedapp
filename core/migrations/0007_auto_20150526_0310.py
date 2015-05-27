# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_location_position'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='outdoor',
            new_name='Custom_Patterns',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='outlets',
            new_name='Edge',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='alcohol',
            new_name='Experience',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='wifi',
            new_name='Mow',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='coffee',
            new_name='Rate',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='food',
            new_name='Responsiveness',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='bathrooms',
            new_name='Scoop_Poop',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='seating',
            new_name='Trim',
        ),
    ]
