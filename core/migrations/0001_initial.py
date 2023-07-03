# Generated by Django 4.2.2 on 2023-06-27 16:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default='2023-06-27 21:29:07')),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(max_length=144, null=True)),
                ('first_name', models.CharField(max_length=244, null=True)),
                ('last_name', models.CharField(max_length=244, null=True)),
                ('email', models.CharField(max_length=244, null=244)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default='2023-06-27 21:29:07')),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('profile_picture', models.ImageField(null=True, upload_to='employees/')),
                ('first_name', models.CharField(max_length=244, null=True)),
                ('last_name', models.CharField(max_length=244, null=True)),
                ('email', models.CharField(max_length=244, null=True)),
                ('mobile', models.CharField(max_length=244, null=True)),
                ('address', models.CharField(max_length=244, null=True)),
                ('city', models.CharField(max_length=144, null=True)),
                ('salary', models.CharField(max_length=244, null=True)),
                ('designation', models.CharField(max_length=244, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default='2023-06-27 21:29:07')),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=244, null=True)),
                ('description', models.TextField(default='null', null=True)),
                ('type', models.CharField(choices=[('general', 'general'), ('expense', 'expense'), ('profit', 'profit')], max_length=244, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default='2023-06-27 21:29:07')),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=244, null=True)),
                ('description', models.TextField()),
                ('duration_start', models.DateField(null=True)),
                ('duration_end', models.DateField(null=True)),
                ('amount', models.CharField(max_length=244, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.client')),
                ('members', models.ManyToManyField(to='core.employee')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default='2023-06-27 21:29:07')),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=244, null=True)),
                ('description', models.TextField(null=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed')], max_length=100, null=True)),
                ('assigned_to', models.ManyToManyField(to='core.employee')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.project')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SalaryInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default='2023-06-27 21:29:07')),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=244, null=True)),
                ('amount', models.CharField(max_length=244, null=True)),
                ('status', models.CharField(choices=[('due', 'due'), ('paid', 'paid')], max_length=244, null=True)),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.employee')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default='2023-06-27 21:29:07')),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=244, null=True)),
                ('amount', models.CharField(max_length=244, null=True)),
                ('status', models.CharField(choices=[('due', 'due'), ('paid', 'paid')], max_length=244, null=True)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.project')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default='2023-06-27 21:29:07')),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('leave', 'leave')], max_length=144, null=True)),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.employee')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]