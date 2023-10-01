# Generated by Django 4.2.5 on 2023-09-29 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_alter_teachers_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachers',
            name='department',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='teachers',
            name='firstname',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='teachers',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='teachers',
            name='lastname',
            field=models.CharField(default='', max_length=255),
        ),
    ]
