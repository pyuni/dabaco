# Generated by Django 5.0.6 on 2024-11-07 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_staticcontentclass_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoryclass',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
