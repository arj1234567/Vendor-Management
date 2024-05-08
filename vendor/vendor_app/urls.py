from django.urls import path
from .views import Vendorview,Purchaseview
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('vendor/',Vendorview.as_view()),
    path('vendor/<int:id>',Vendorview.as_view()),
    path('purchase/',Purchaseview.as_view()),
    path('purchase/<int:id>',Purchaseview.as_view()),
    path('vendor/<int:vendor_id>/performance/',Purchaseview.as_view()),
    path('purchase_orders/<int:id>/acknowledge/', csrf_exempt(Purchaseview.as_view())),
]
