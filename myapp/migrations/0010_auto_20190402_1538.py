# Generated by Django 2.1.7 on 2019-04-02 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_sellingitems_sell_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sellingitems',
            name='sell_id',
        ),
        migrations.AddField(
            model_name='sellingitems',
            name='sell_username',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]