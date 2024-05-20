# Generated by Django 5.0.3 on 2024-03-15 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category_one', models.CharField(max_length=100, null=True, verbose_name='Category_one')),
                ('subcategory_one', models.CharField(max_length=100, null=True, verbose_name='Subcategory_one')),
                ('category_two', models.CharField(max_length=100, null=True, verbose_name='Category_two')),
                ('subcategory_two', models.CharField(max_length=100, null=True, verbose_name='Subcategory_two')),
                ('type', models.CharField(max_length=50, null=True, verbose_name='Type')),
                ('file_id', models.CharField(max_length=100, null=True, verbose_name='File ID')),
                ('caption', models.TextField(max_length=4000, null=True, verbose_name='Caption')),
                ('description', models.TextField(max_length=4000, null=True, verbose_name='Description')),
                ('media_group', models.BooleanField(default=False, verbose_name='Media group')),
                ('callback', models.CharField(max_length=60, null=True, verbose_name='Callback')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, null=True, verbose_name='Telegram username')),
                ('telegram_id', models.BigIntegerField(default=1, unique=True, verbose_name='Telegram ID')),
            ],
        ),
    ]
