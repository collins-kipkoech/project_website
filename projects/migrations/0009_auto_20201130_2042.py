# Generated by Django 3.1.3 on 2020-11-30 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20201130_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='link',
            field=models.CharField(max_length=500),
        ),
    ]
