# Generated by Django 4.2.2 on 2023-09-05 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('extra_cheese_added', models.BooleanField(default=False)),
                ('extra_toppings_added', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='DeluxePizza',
            fields=[
                ('pizza_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.pizza')),
            ],
            bases=('main.pizza',),
        ),
    ]