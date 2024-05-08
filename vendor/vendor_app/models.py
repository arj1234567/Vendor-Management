from django.db import models

class Vendor_tb(models.Model):
    Name = models.CharField(max_length=20)
    Contact_details = models.TextField(max_length=20)
    Address = models.TextField(max_length =20)
    Vendor_code = models.CharField(max_length=20)
    On_time_delivery = models.FloatField()
    Quality_rating_average = models.FloatField()
    Average_response_time = models.FloatField()
    Fullfillment_rate = models.FloatField()

class Purchase_order_tb(models.Model):
    PO_number = models.CharField(max_length =20)
    Vendor_id = models.ForeignKey(Vendor_tb,on_delete=models.CASCADE)
    Order_date = models.DateTimeField()
    Delivery_date = models.DateTimeField()
    Items = models.JSONField()
    Quantity = models.IntegerField()
    Status = models.CharField(max_length=20)
    Quality_rating = models.FloatField()
    Issue_date = models.DateTimeField()
    Acknowledgement_rate = models.DateTimeField()
    
class Historical_performance_tb(models.Model):
    Vendor_id = models.ForeignKey(Vendor_tb,related_name='vendorid',on_delete=models.CASCADE)
    Date = models.DateTimeField()
    On_time_delivery_rate = models.FloatField()
    Quality_rating_average = models.FloatField()
    Average_response_time = models.FloatField()
    Fullfillment_rate = models.FloatField()
    

# Create your models here.
