# Generated by Django 3.2 on 2021-05-05 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_project_solution'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='solution',
        ),
        migrations.AddField(
            model_name='project',
            name='contribution',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
