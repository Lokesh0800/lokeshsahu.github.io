# Generated by Django 4.0.5 on 2022-07-04 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0005_alter_employeedata_emp_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeedata',
            name='id',
        ),
        migrations.AlterField(
            model_name='employeedata',
            name='Emp_id',
            field=models.IntegerField(default='1', primary_key=True, serialize=False),
        ),
    ]
