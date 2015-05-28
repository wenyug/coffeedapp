# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20150526_0310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='Custom_Patterns',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'Yes'), (1, b'No')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='Edge',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'Yes'), (1, b'No')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='Experience',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'First Summer'), (1, b'1-3 years'), (2, b'3-5 years'), (3, b'5 + years')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='Mow',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'Yes'), (1, b'No')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='Rate',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'$.75-$1.00/min'), (1, b'$1.00-$1.25/min'), (2, b'$1.25-$1.50/min'), (3, b'$1.50-$1.75/min'), (4, b'$1.75+/min')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='Responsiveness',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'Today'), (1, b'Next 3 Days'), (2, b'Next Week')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='Scoop_Poop',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'Yes'), (1, b'No')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='Trim',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'Yes'), (1, b'No')]),
        ),
    ]
