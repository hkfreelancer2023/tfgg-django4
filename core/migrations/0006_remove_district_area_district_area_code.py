# Generated by Django 4.2.6 on 2023-10-25 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_district_createdat_remove_district_lastupdate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='district',
            name='area',
        ),
        migrations.AddField(
            model_name='district',
            name='area_code',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.area', to_field='area_code'),
            preserve_default=False,
        ),
    ]