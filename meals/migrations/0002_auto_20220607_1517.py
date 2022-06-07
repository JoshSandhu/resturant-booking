# Generated by Django 3.2.13 on 2022-06-07 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='meals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('description', models.TextField(max_length=200)),
                ('size', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('prep_time', models.Field()),
                ('image', models.ImageField(upload_to='')),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'meal',
                'verbose_name_plural': 'meals',
            },
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
    ]