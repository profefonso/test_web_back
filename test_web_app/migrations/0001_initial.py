# Generated by Django 2.1.7 on 2019-02-14 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('iso_district_code', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('comments', models.CharField(max_length=100)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='test_web_app.District')),
            ],
        ),
    ]
