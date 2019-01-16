# Generated by Django 2.1.5 on 2019-01-16 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ferien', '0002_auto_20190111_1040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100, verbose_name='Country')),
                ('region', models.CharField(blank=True, max_length=100, verbose_name='Region')),
                ('iso', models.CharField(blank=True, max_length=6, verbose_name='ISO Code')),
                ('region_type', models.CharField(blank=True, choices=[('s', 'State'), ('p', 'Province'), ('', 'No Regions defined')], max_length=1, verbose_name='Region Type')),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
                'ordering': ['iso'],
            },
        ),
        migrations.AlterField(
            model_name='schoolholidays',
            name='country',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ferien.Country', verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='schoolholidays',
            name='name',
            field=models.CharField(choices=[('OF', 'Osterferien'), ('PF', 'Pfingstferien'), ('SF', 'Sommerferien'), ('HF', 'Herbstferien'), ('WF', 'Weihnachtsferien')], default='SF', max_length=100, verbose_name='Holidays'),
        ),
    ]
