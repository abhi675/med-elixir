# Generated by Django 3.1.6 on 2021-07-04 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_details_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anthologies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anthology_name', models.CharField(max_length=50)),
                ('logo', models.ImageField(upload_to='anthology')),
            ],
        ),
    ]