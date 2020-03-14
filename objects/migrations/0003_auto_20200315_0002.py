# Generated by Django 3.0.4 on 2020-03-14 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0002_auto_20200314_2253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=28)),
                ('phone', models.PositiveIntegerField()),
                ('addres', models.CharField(max_length=128)),
                ('total_price', models.PositiveIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='productinbasket',
            name='numb',
            field=models.PositiveIntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='productinbasket',
            name='price_for_one',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='productinbasket',
            name='total_price',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
