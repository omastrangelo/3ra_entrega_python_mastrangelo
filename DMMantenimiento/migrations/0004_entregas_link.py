# Generated by Django 4.2.5 on 2023-09-09 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DMMantenimiento', '0003_entregas'),
    ]

    operations = [
        migrations.AddField(
            model_name='entregas',
            name='link',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
