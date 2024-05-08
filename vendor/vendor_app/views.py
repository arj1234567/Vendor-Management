from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import VendorSerializer,PurchaseOrderSerializer
from rest_framework.response import Response
from .models import *
from rest_framework import status
from django.db.models import F,Avg
from datetime import timedelta,timezone
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.utils import timezone

class Vendorview(APIView):
    def post(self,request):
        serializer = VendorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':serializer.data},status=status.HTTP_201_CREATED)
        else:
            return Response({'status':'error','data':serializer.data},status=status.HTTP_400_BAD_REQUEST)
        
    def get(self,request,id=None):
        if id:
            vendor = Vendor_tb.objects.get(id=id)
            serializer = VendorSerializer(vendor)
            return Response({'status':'success','data':serializer.data},status=status.HTTP_200_OK)
        vendor = Vendor_tb.objects.all()
        serializer = VendorSerializer(vendor,many=True)
        return Response({'status':'success','data':serializer.data},status=status.HTTP_200_OK)
    
    def patch(self,request,id=None):
        vendor = Vendor_tb.objects.get(id=id)
        serializer = VendorSerializer(vendor,data = request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':serializer.data},status=status.HTTP_200_OK)
        else:
            return Response({'status':'error','data':serializer.data},status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id=None):
        vendor = Vendor_tb.objects.get(id=id)
        vendor.delete()
        return Response({'status':'success','message':'vendor deleted succesfully'},status=status.HTTP_200_OK)
    
class Purchaseview(APIView):
    

    def patch(self,request,id=None):
        purchase = Purchase_order_tb.objects.get(id=id)
        serializer = PurchaseOrderSerializer(purchase,data = request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':serializer.data},status=status.HTTP_200_OK)
        else:
            return Response({'status':'error','data':serializer.data},status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id=None):
        purchase = Purchase_order_tb.objects.get(id=id)
        purchase.delete()
        return Response({'status':'success','message':'purchase deleted succesfully'},status=status.HTTP_200_OK)
    
    def ontime_delivery_rate(self,vendor_id):
        completed_pos = Purchase_order_tb.objects.filter(Vendor_id=vendor_id,Status="completed")
        total_completed = completed_pos.count()
        if total_completed ==  0:
            return 0
        ontime_delivered = completed_pos.filter(Delivery_date__lte = F('Acknowledgement_rate'))
        ontime_delivered_rate = ontime_delivered.count()/total_completed
        return ontime_delivered_rate
    
    def quality_average_rate(self,vendor_id):
        completed_with_rating = Purchase_order_tb.objects.filter(Vendor_id=vendor_id,Status="completed",Quality_rating__isnull = False)
        quality_rating_avg = completed_with_rating.aggregate(quality_rating_avg=Avg('Quality_rating'))['quality_rating_avg']
        return quality_rating_avg or 0
    
    def average_response_time(self,vendor_id):
        acknowledgement_pos = Purchase_order_tb.objects.filter(Vendor_id = vendor_id,Acknowledgement_rate__isnull=False)
        total_response_time = timedelta(seconds=0)
        total_acknowledged_pos = 0
        for i in acknowledgement_pos:
            if i.Acknowledgement_rate and i.Issue_date:
                total_response_time += i.Acknowledgement_rate - i.Issue_date
                total_acknowledged_pos=total_acknowledged_pos+1
        avg_response_time = total_response_time.total_seconds()/total_acknowledged_pos if total_acknowledged_pos>0 else 0
        return avg_response_time
    
    def fullfillment_rate(self,vendor_id):
        total_pos = Purchase_order_tb.objects.filter(Vendor_id = vendor_id)
        fullfilled_pos = total_pos.filter(Status="completed",Quality_rating__isnull = False)
        fullfillment_rate = fullfilled_pos.count()/total_pos.count() if total_pos.count() else 0
        return fullfillment_rate
    
    def store_performance_metrics(self, vendor_id):
        ontime_delivery_rate = self.ontime_delivery_rate(vendor_id)
        quality_rating_avg = self.quality_average_rate(vendor_id)
        average_response_time = self.average_response_time(vendor_id)
        fulfillment_rate = self.fullfillment_rate(vendor_id)

        historical_performance = Historical_performance_tb(
            Vendor_id_id=vendor_id,
            Date=timezone.now(),
            On_time_delivery_rate=ontime_delivery_rate,
            Quality_rating_average=quality_rating_avg,
            Average_response_time=average_response_time,
            Fullfillment_rate=fulfillment_rate
        )
        historical_performance.save()
    
    
    def get(self,request,vendor_id=None,id=None):
        if vendor_id:
            self.store_performance_metrics(vendor_id)
            ontime_delivery_rate = self.ontime_delivery_rate(vendor_id)
            quality_rating_avg = self.quality_average_rate(vendor_id)
            average_response_time = self.average_response_time(vendor_id)
            fulfillment_rate = self.fullfillment_rate(vendor_id)
            return Response({
                'ontime_delivery_rate': ontime_delivery_rate,
                'quality_rating_avg': quality_rating_avg,
                'average_response_time': average_response_time,
                'fullfillment_rate': fulfillment_rate
            }, status=status.HTTP_200_OK)
        elif id:
            purchase = Purchase_order_tb.objects.get(id=id)
            serializer = PurchaseOrderSerializer(purchase)
            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            purchase = Purchase_order_tb.objects.all()
            serializer = PurchaseOrderSerializer(purchase,many=True)
            return Response({'status':'success','data':serializer.data},status=status.HTTP_200_OK)
        
        
    
        
    @method_decorator(csrf_exempt)
    def post(self, request, id=None):
        if id:
            purchase = Purchase_order_tb.objects.get(id=id)
            purchase.Acknowledgement_rate = timezone.now()
            purchase.save() 
            vendor_id = purchase.Vendor_id_id
            vendor = Vendor_tb.objects.get(id=vendor_id)
            acknowledgement_pos = Purchase_order_tb.objects.filter(Vendor_id_id=vendor_id, Acknowledgement_rate__isnull=False)
            total_response_time = timedelta(seconds=0)
            total_acknowledged_pos = 0
            for pos in acknowledgement_pos:
                if pos.Acknowledgement_rate and pos.Issue_date:
                    total_response_time += pos.Acknowledgement_rate - pos.Issue_date
                    total_acknowledged_pos += 1
            avg_response_time = total_response_time.total_seconds() / total_acknowledged_pos if total_acknowledged_pos > 0 else 0
            vendor.Average_response_time = avg_response_time
            vendor.save()
        
            return Response({'status': 'success', 'message': 'Purchase order acknowledged successfully','avg_response_time':avg_response_time}, status=status.HTTP_200_OK)
        else:
            serializer = PurchaseOrderSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':'success','data': serializer.data},status=status.HTTP_201_CREATED)
            else:
                return Response({'status':'error','data':serializer.data},status=status.HTTP_400_BAD_REQUEST)
            


            
    
    
    
        
            
# Create your views here.
