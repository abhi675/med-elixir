# Generated by Django 3.1.6 on 2021-07-04 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0004_anthologies'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pics')),
            ],
        ),
    ]