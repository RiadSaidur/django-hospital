# Generated by Django 3.0.4 on 2020-03-22 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_auto_20200321_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='fullname',
            field=models.CharField(max_length=50, null=True),
        ),
    ]