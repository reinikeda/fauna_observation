# Generated by Django 4.1.7 on 2023-03-13 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faunaweb', '0004_alter_mammalsclass_class_id_reptilesclass_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rayfinnedfishesclass',
            name='class_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='rayfinnedfishes', to='faunaweb.animalclass', verbose_name='animal class'),
        ),
    ]
