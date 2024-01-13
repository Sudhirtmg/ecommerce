# Generated by Django 4.2.7 on 2023-11-20 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_category_main_category_alter_banner_discount_deals_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Quantity', models.IntegerField()),
                ('Product_Availability', models.IntegerField()),
                ('Product_Image', models.CharField(max_length=200)),
                ('Product_Name', models.CharField(max_length=200)),
                ('Product_Informations', models.CharField(max_length=200)),
                ('Product_Price', models.IntegerField()),
                ('Product_Discount', models.IntegerField()),
                ('Product_Descriptions', models.CharField(max_length=200)),
                ('Tags', models.CharField(max_length=200)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='banner',
            name='Discount_Deals',
            field=models.CharField(choices=[('HOT DEALS', 'HOT_DEALS'), ('FULLY DISCOUNT', 'FULLY_DISCOUNT'), ('NEW ARRIVAL', 'NEW ARRIVAL')], max_length=200),
        ),
        migrations.AlterField(
            model_name='slider',
            name='Discount_Deals',
            field=models.CharField(choices=[('HOT DEALS', 'HOT_DEALS'), ('FULLY DISCOUNT', 'FULLY_DISCOUNT'), ('NEW ARRIVAL', 'NEW ARRIVAL')], max_length=200),
        ),
        migrations.CreateModel(
            name='Product_Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image_Url', models.CharField(max_length=200)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.section'),
        ),
        migrations.CreateModel(
            name='Additional_Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Specifications', models.CharField(max_length=200)),
                ('Details', models.CharField(max_length=200)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
            ],
        ),
    ]