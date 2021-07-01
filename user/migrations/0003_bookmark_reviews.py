# Generated by Django 3.2.4 on 2021-07-01 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laundry', '0002_delete_reviews'),
        ('user', '0002_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.FloatField(default=0.0)),
                ('content', models.TextField()),
                ('laundry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laundry.laundry')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('laundry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laundry.laundry')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
