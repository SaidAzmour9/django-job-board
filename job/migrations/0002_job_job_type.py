# Generated by Django 4.1.5 on 2023-01-25 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('full time', 'full time'), ('part time', 'part time')], default='', max_length=15),
            preserve_default=False,
        ),
    ]
