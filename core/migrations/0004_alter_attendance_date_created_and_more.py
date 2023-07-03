# Generated by Django 4.2.2 on 2023-06-27 16:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_salaryinvoice_person_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 27, 21, 57, 58, 459835)),
        ),
        migrations.AlterField(
            model_name='client',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 27, 21, 57, 58, 459835)),
        ),
        migrations.AlterField(
            model_name='employee',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 27, 21, 57, 58, 459835)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 27, 21, 57, 58, 459835)),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 27, 21, 57, 58, 459835)),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 27, 21, 57, 58, 459835)),
        ),
        migrations.CreateModel(
            name='SalaryInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=datetime.datetime(2023, 6, 27, 21, 57, 58, 459835))),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=244, null=True)),
                ('amount', models.CharField(max_length=244, null=True)),
                ('status', models.CharField(choices=[('due', 'due'), ('paid', 'paid')], max_length=244, null=True)),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.employee')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=datetime.datetime(2023, 6, 27, 21, 57, 58, 459835))),
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
    ]