# Generated by Django 3.0.8 on 2021-12-20 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('JobsApp', '0007_auto_20211220_1607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job_upload',
            name='About_Company',
        ),
        migrations.RemoveField(
            model_name='job_upload',
            name='Job_Skills',
        ),
        migrations.RemoveField(
            model_name='job_upload',
            name='Offer_Types',
        ),
        migrations.RemoveField(
            model_name='job_upload',
            name='Required_Skills',
        ),
        migrations.RemoveField(
            model_name='job_upload',
            name='Skill_Set',
        ),
    ]