# Generated by Django 4.2.20 on 2025-04-06 02:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('survey_app', '0002_alter_surveysubmission_chosen_redirection'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveysubmission',
            name='submitted_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='surveysubmission',
            name='chosen_redirection',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
