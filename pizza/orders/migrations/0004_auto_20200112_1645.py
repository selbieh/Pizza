# Generated by Django 2.2.9 on 2020-01-12 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20200112_1638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderpizzaitem',
            name='toOrder',
        ),
        migrations.AddField(
            model_name='order',
            name='orderObjects',
            field=models.ManyToManyField(null=True, to='orders.orderPizzaItem'),
        ),
        migrations.AlterField(
            model_name='orderpizzaitem',
            name='pizza',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='servedPizz.servedPizza'),
        ),
        migrations.AlterField(
            model_name='orderpizzaitem',
            name='size',
            field=models.CharField(choices=[('medium', 'medium'), ('small', 'small'), ('large', 'large')], max_length=10),
        ),
    ]
