# Generated by Django 2.1 on 2018-08-24 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20180824_0134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='julian',
            new_name='julian_end',
        ),
        migrations.RemoveField(
            model_name='event',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='event',
            name='start_date',
        ),
        migrations.AddField(
            model_name='event',
            name='julian_start',
            field=models.CharField(choices=[('AD', 'anno Domini'), ('BC', 'before Christ')], default='AD', max_length=2, verbose_name='Julian'),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_month',
            field=models.IntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')], default='01', verbose_name='End Month'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_month',
            field=models.IntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')], default='01', verbose_name='Start Month'),
        ),
    ]