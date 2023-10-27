# Generated by Django 4.2.6 on 2023-10-25 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_area_area_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_code', models.CharField(blank=True, max_length=8, unique=True, verbose_name='District Code')),
                ('district_name', models.CharField(blank=True, max_length=50, verbose_name='District Name')),
                ('district_name_zh_hk', models.CharField(blank=True, max_length=50, verbose_name='District Chinese Name')),
                ('createdat', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created at')),
                ('lastupdate', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Last update Time')),
                ('area_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.area', to_field='area_code')),
            ],
            options={
                'verbose_name_plural': 'Districts',
                'ordering': ['id'],
            },
        ),
    ]
