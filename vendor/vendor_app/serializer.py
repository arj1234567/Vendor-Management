from rest_framework import serializers
from .models import *

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor_tb
        fields = ['id', 'Name', 'Contact_details', 'Address', 'Vendor_code', 'On_time_delivery',
                  'Quality_rating_average', 'Average_response_time', 'Fullfillment_rate']

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase_order_tb
        fields = ['id', 'PO_number', 'Vendor_id', 'Order_date', 'Delivery_date', 'Items', 'Quantity',
                  'Status', 'Quality_rating', 'Issue_date', 'Acknowledgement_rate']

class HistoricalPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historical_performance_tb
        fields = ['id', 'Vendor_id', 'Date', 'On_time_delivery_rate', 'Quality_rating_average',
                  'Average_response_time', 'Fullfillment_rate']
