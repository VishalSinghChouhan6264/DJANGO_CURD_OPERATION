# Generated by Django 4.2.7 on 2023-12-14 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('before', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='demo',
            name='contact_num',
            field=models.IntegerField(null=True),
        ),
    ]