# Generated by Django 4.2.5 on 2023-11-15 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmstu_lab', '0003_alter_miningservices_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestService',
            fields=[
                ('requestid', models.AutoField(primary_key=True, serialize=False)),
                ('serviceid_field', models.IntegerField()),
            ],
            options={
                'db_table': 'request_service',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('iduser', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.TextField(max_length=30)),
                ('email_field', models.TextField(max_length=30)),
                ('password_field', models.TextField(max_length=30)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]
