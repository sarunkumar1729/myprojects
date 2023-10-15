# Generated by Django 4.2.6 on 2023-10-14 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_rename_email_bill_model_email1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bill_model',
            old_name='HSNorSAC',
            new_name='Email2',
        ),
        migrations.RemoveField(
            model_name='bill_model',
            name='id',
        ),
        migrations.AddField(
            model_name='bill_model',
            name='CentralTax',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='bill_model',
            name='GSTIN2',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='bill_model',
            name='HSN',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='bill_model',
            name='SAC',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='bill_model',
            name='StateTax',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='bill_model',
            name='adress',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bill_model',
            name='InvoiceNo',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bill_model',
            name='Total',
            field=models.FloatField(null=True),
        ),
    ]