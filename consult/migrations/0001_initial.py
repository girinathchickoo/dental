# Generated by Django 3.0.7 on 2020-07-02 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientData',
            fields=[
                ('date', models.DateField(auto_now_add=True, db_column='Date')),
                ('mobile_no', models.CharField(db_column='mobileno', max_length=10, primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(db_column='firstname', max_length=15)),
                ('last_name', models.CharField(db_column='lastname', max_length=15)),
                ('age', models.IntegerField(db_column='age')),
                ('sex', models.CharField(db_column='sex', max_length=1)),
                ('blood_group', models.CharField(db_column='bloodgroup', max_length=4)),
                ('chief_complaint', models.TextField(db_column='chief_complaint', max_length=200)),
                ('medical_history', models.TextField(db_column='medical_history', max_length=200)),
                ('clinical_findings', models.TextField(db_column='clinical_findings', max_length=200)),
                ('investigation', models.TextField(db_column='investigation', max_length=200)),
                ('diagnosis', models.TextField(db_column='diagnosis', max_length=200)),
                ('prescription', models.TextField(db_column='prescription', max_length=200)),
                ('next_review_date', models.CharField(db_column='review date', max_length=200)),
            ],
        ),
    ]
