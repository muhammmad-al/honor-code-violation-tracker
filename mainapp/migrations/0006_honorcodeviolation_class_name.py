# Generated by Django 4.2.10 on 2024-04-24 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_honorcodeviolation_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='honorcodeviolation',
            name='class_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
