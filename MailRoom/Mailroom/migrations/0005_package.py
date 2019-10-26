# Generated by Django 2.1.5 on 2019-01-14 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mailroom', '0004_auto_20190114_2016'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Number', models.IntegerField()),
                ('Company', models.CharField(max_length=50)),
                ('RollNo', models.CharField(max_length=30)),
                ('Phone', models.IntegerField(max_length=12)),
            ],
        ),
    ]