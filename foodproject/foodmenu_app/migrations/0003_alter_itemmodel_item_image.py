# Generated by Django 4.1 on 2023-04-13 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodmenu_app', '0002_itemmodel_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemmodel',
            name='item_image',
            field=models.CharField(default='https://media-cldnry.s-nbcnews.com/image/upload/t_fit-1240w,f_auto,q_auto:best/streams/2014/May/140501/2D274905752676-setting860.png', max_length=500),
        ),
    ]