# Generated by Django 4.2.20 on 2025-04-06 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveysubmission',
            name='chosen_redirection',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
