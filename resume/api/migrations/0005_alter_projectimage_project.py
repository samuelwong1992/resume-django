# Generated by Django 3.2 on 2021-05-04 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_projectimage_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectimage',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.project', verbose_name='project'),
        ),
    ]
