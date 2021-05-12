# Generated by Django 3.2.2 on 2021-05-11 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(default='', max_length=100)),
                ('advisor_id', models.CharField(default='', max_length=100)),
                ('booking_date_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
