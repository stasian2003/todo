# Generated by Django 3.1.5 on 2021-01-24 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=100)),
                ('discription', models.CharField(max_length=1000)),
                ('price', models.CharField(max_length=10)),
                ('genre', models.CharField(max_length=80)),
                ('author', models.CharField(max_length=80)),
                ('year', models.CharField(max_length=4)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
