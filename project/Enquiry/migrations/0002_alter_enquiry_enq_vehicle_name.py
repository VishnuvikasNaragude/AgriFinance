# Generated by Django 5.1.4 on 2024-12-14 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Enquiry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='enq_vehicle_name',
            field=models.CharField(choices=[('Single', 'Single'), ('Married', 'Married')], max_length=250),
        ),
    ]
