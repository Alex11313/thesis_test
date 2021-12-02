# Generated by Django 3.2.6 on 2021-12-02 17:50

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('surname', models.CharField(max_length=50, verbose_name='Surname')),
                ('patronymic', models.CharField(blank=True, max_length=50, null=True, verbose_name='Patronymic')),
                ('position', models.CharField(blank=True, max_length=100, null=True, verbose_name='Position')),
                ('salary', models.FloatField(blank=True, null=True, verbose_name='Salary')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='Age')),
                ('photo', models.FileField(blank=True, null=True, upload_to='Employee/photo', verbose_name='Photo')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.department')),
            ],
        ),
    ]