# Generated by Django 3.0.4 on 2020-03-14 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0003_auto_20200315_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinbasket',
            name='order',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='objects.Order'),
        ),
    ]
