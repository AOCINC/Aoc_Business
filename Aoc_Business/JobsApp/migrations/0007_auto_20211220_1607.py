# Generated by Django 3.0.8 on 2021-12-20 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobsApp', '0006_job_upload_freelancing'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_upload',
            name='About_Company',
            field=models.CharField(default=' ', max_length=250),
        ),
        migrations.AddField(
            model_name='job_upload',
            name='Job_Skills',
            field=models.CharField(default=' ', max_length=250),
        ),
        migrations.AddField(
            model_name='job_upload',
            name='Offer_Types',
            field=models.CharField(default='permanent', max_length=250),
        ),
        migrations.AddField(
            model_name='job_upload',
            name='Required_Skills',
            field=models.CharField(default=' ', max_length=250),
        ),
        migrations.AddField(
            model_name='job_upload',
            name='Skill_Set',
            field=models.CharField(default=' ', max_length=250),
        ),
    ]
