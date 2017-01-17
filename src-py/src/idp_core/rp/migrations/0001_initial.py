# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-04 06:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oidc_provider', '0016_userconsent_and_verbosenames'),
    ]

    operations = [
        migrations.CreateModel(
            name='RpInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='oidc_provider.Client')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rps', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'relaying party detail',
                'verbose_name_plural': 'relaying parties details',
            },
        ),
    ]