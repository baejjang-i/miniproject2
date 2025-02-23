from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laundry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('laundry_name', models.CharField(max_length=30)),
                ('laundry_address', models.TextField()),
                ('laundry_road', models.TextField()),
                ('laundry_lat', models.FloatField()),
                ('laundry_lng', models.FloatField()),
                ('laundry_tel', models.TextField()),
                ('laundry_img', models.CharField(max_length=100)),
                ('laundry_page', models.TextField()),
                ('washer_cnt', models.IntegerField()),
                ('dryer_cnt', models.IntegerField()),
            ],
            options={
                'db_table': 'laundry',
            },
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_name', models.CharField(max_length=100)),
                ('add_fee', models.IntegerField()),
                ('laundry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laundry.laundry')),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('useable', models.BooleanField()),
                ('machine_category', models.IntegerField()),
                ('machine_type', models.IntegerField()),
                ('basic_rate', models.IntegerField()),
                ('laundry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laundry.laundry')),
            ],
        ),
    ]
