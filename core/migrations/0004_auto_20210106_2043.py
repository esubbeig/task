# Generated by Django 2.2.6 on 2021-01-06 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_dataresult'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataresult',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Category'),
        ),
        migrations.AlterField(
            model_name='dataresult',
            name='sub_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.SubCategory'),
        ),
    ]