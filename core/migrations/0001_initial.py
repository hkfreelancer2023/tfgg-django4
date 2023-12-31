# Generated by Django 4.2.6 on 2023-10-25 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_name', models.CharField(blank=True, max_length=50, verbose_name='Area Name')),
                ('area_name_zh_hk', models.CharField(blank=True, max_length=50, verbose_name='Area Chinese Name')),
                ('createdat', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created at')),
                ('lastupdate', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Last update Time')),
            ],
            options={
                'verbose_name_plural': 'Area',
                'ordering': ['id'],
            },
        ),
    ]
