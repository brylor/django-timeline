# Generated by Django 2.1 on 2018-08-24 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20180824_0132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='status',
        ),
        migrations.AddField(
            model_name='event',
            name='julian',
            field=models.CharField(choices=[('AD', 'anno Domini'), ('BC', 'before Christ')], default='AD', max_length=2, verbose_name='Julian'),
        ),
    ]