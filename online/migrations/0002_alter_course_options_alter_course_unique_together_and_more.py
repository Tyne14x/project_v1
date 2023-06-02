# Generated by Django 4.0.4 on 2023-01-18 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='course',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='course',
            name='facultyKey',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='course',
            name='studentKey',
            field=models.IntegerField(),
        ),
    ]
