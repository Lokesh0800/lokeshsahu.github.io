# Generated by Django 4.0.5 on 2022-06-24 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0002_alter_employeedata_emp_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedata',
            name='Emp_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='employeedata',
            name='Emp_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employeedata',
            name='contact',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='employeedata',
            name='department',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeedata',
            name='designation',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeedata',
            name='doj',
            field=models.DateField(null=True),
        ),
    ]
