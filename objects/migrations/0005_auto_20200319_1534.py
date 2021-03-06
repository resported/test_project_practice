# Generated by Django 3.0.4 on 2020-03-19 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0004_productinbasket_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.AddField(
            model_name='product',
            name='men',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(allow_unicode=True, default=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='woman',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='addres',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='productinbasket',
            name='order',
            field=models.ForeignKey(blank=True, default=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='objects.Order'),
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.PROTECT, to='objects.Type'),
        ),
    ]
