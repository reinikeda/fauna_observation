# Generated by Django 4.1.7 on 2023-03-13 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_scientific', models.CharField(max_length=200, verbose_name='class scientific name')),
                ('class_en', models.CharField(max_length=200, verbose_name='class english name')),
                ('class_national', models.CharField(max_length=200, verbose_name='class national name')),
            ],
            options={
                'verbose_name': 'animal class',
                'verbose_name_plural': 'animal classes',
                'ordering': ['class_scientific'],
            },
        ),
        migrations.CreateModel(
            name='MammalsClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_scientific', models.CharField(max_length=200, verbose_name='order scientific name')),
                ('family_scientific', models.CharField(max_length=200, verbose_name='family scientific name')),
                ('order_national', models.CharField(blank=True, max_length=200, null=True, verbose_name='order national name')),
                ('species_scientific', models.CharField(max_length=200, verbose_name='species scientific name')),
                ('species_en', models.CharField(blank=True, max_length=200, null=True, verbose_name='species english name')),
                ('species_national', models.CharField(blank=True, max_length=200, null=True, verbose_name='species national name')),
                ('endangered', models.BooleanField(default=False, verbose_name='endangered species')),
                ('species_image', models.ImageField(blank=True, null=True, upload_to='faunaweb/species/', verbose_name='species image')),
                ('animal_class', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='animal_classes', to='faunaweb.animalclass', verbose_name='animal class')),
            ],
            options={
                'verbose_name': 'mammals class species',
                'verbose_name_plural': 'mammals class species',
                'ordering': ['order_scientific', 'species_scientific'],
            },
        ),
    ]
