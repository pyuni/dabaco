# Generated by Django 5.0.6 on 2024-11-07 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staticcontentclass',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]