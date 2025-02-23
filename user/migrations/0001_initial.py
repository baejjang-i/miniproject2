
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('laundry', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20)),
                ('user_pw', models.CharField(max_length=20)),
                ('user_name', models.CharField(max_length=20)),
                ('user_nick', models.CharField(max_length=20, unique=True)),
                ('user_email', models.EmailField(max_length=254, unique=True)),
                ('user_phone', models.CharField(max_length=20, unique=True)),
                ('user_address', models.TextField()),
                ('user_lat', models.FloatField(null=True)),
                ('user_lng', models.FloatField(null=True)),
                ('isEmailAlert', models.BooleanField(default=True)),
                ('isPhoneAlert', models.BooleanField(default=True)),
                ('isTempPW', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.FloatField(default=0.0)),
                ('review_content', models.TextField()),
                ('laundry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laundry.laundry')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_num', models.CharField(max_length=20)),
                ('validate_dt', models.DateField()),
                ('card_holder', models.CharField(max_length=20)),
                ('card_pw', models.CharField(max_length=20)),
                ('card_cvc', models.CharField(max_length=5)),
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
