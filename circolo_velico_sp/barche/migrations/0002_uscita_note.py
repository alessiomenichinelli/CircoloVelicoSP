# Generated by Django 4.2.1 on 2023-09-30 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barche', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uscita',
            name='note',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
