# Generated by Django 3.2.6 on 2021-12-03 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_auto_20211202_1921'),
        ('project', '0002_alter_project_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='boss',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_host', to='employees.employee'),
        ),
    ]
