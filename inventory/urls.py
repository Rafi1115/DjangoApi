from django.urls import path 

from .import views

app_name = 'product'

urlpatterns = [

    path('inventory/', views.Product_List.as_view(), name='product_list'),
    path('inventory/<id>/', views.product_detail, name='product_detail' ),

]