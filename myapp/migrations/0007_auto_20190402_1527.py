# Generated by Django 2.1.7 on 2019-04-02 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20190402_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellingitems',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sellingitems',
            name='sell_id',
            field=models.IntegerField(),
        ),
    ]
