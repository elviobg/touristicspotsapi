# Generated by Django 2.0.7 on 2018-07-31 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20180730_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='spot',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='spots'),
        ),
    ]
