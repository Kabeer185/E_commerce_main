# Generated by Django 5.1 on 2025-01-15 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0011_remove_slider_product_delete_promotions_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='promotion_product',
            field=models.BooleanField(default=False, help_text='@-default,1-Promotion'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='slider_product',
            field=models.BooleanField(default=False, help_text='@-default,1-Slider'),
        ),
    ]