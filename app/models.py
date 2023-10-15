from django.db import models

# Create your models here.

class bill_model(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    name=models.CharField(max_length=255)
    GSTIN=models.CharField(max_length=255,null=True)
    UIN=models.CharField(null=True,max_length=255)
    stateName1=models.CharField(max_length=255)
    Email1=models.CharField(max_length=255,null=True)
    Dated1=models.DateField()

    Buyer=models.CharField(max_length=255)
    adress=models.CharField(max_length=255,null=True)
    Email2=models.CharField(max_length=255,null=True)
    phone=models.CharField(max_length=255,null=True)
    GSTIN2=models.CharField(max_length=255,null=True)
    stateName2=models.CharField(max_length=255,null=True)
    ModeORtermsOfPayment=models.CharField(max_length=255)
    OtherReference=models.CharField(max_length=255)
    descriptionOfGoods=models.CharField(max_length=255,null=True)
    HSN=models.CharField(max_length=255,null=True)
    SAC=models.CharField(max_length=255,null=True)
    Rate=models.CharField(max_length=255,null=True)
    per=models.CharField(max_length=255,null=True)
    disc=models.CharField(max_length=255,null=True)
    amount1=models.CharField(max_length=255,null=True)
    CentralTax=models.FloatField(null=True)
    StateTax=models.FloatField(null=True)
    total_tax=models.FloatField(null=True)
    tax_words=models.CharField(max_length=255,null=True)
    Total=models.FloatField(null=True)
    words=models.CharField(max_length=255,null=True)

    class Meta:
        ordering=['created_at']




