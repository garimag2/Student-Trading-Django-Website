# Generated by Django 2.1.7 on 2019-03-30 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_sellingitems_sell_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellingitems',
            name='sell_photo',
            field=models.ImageField(default='', upload_to='pic_folder/'),
        ),
    ]
