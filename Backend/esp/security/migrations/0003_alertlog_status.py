# Generated by Django 3.1.5 on 2021-12-13 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0002_auto_20211213_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='alertlog',
            name='status',
            field=models.CharField(default='success', max_length=50),
            preserve_default=False,
        ),
    ]
