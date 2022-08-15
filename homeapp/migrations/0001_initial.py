# Generated by Django 4.0.5 on 2022-06-24 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Emp_id', models.IntegerField(max_length=10)),
                ('Emp_name', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=20)),
                ('doj', models.DateField()),
                ('contact', models.BigIntegerField(max_length=10)),
            ],
        ),
    ]
