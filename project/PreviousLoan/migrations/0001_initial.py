# Generated by Django 5.1.4 on 2024-12-24 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PreviousLoan',
            fields=[
                ('previousloanId', models.IntegerField(primary_key=True, serialize=False)),
                ('previousLoanamount', models.CharField(max_length=250)),
                ('previousLoanStatus', models.CharField(max_length=250)),
                ('Tenure', models.CharField(max_length=250)),
                ('paidAmount', models.CharField(max_length=250)),
                ('remainingAmount', models.CharField(max_length=250)),
                ('bank', models.CharField(max_length=250)),
            ],
        ),
    ]
