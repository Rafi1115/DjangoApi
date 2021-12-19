from django.urls import path 

from .import views

urlpatterns = [

    path('inventory/', views.ProductListApiView.as_view(), name='api_product_list'),
    path('inventory/<id>/', views.ProductDetailApiView.as_view()),
    path('search/', views.ProductSearchAPIView.as_view()),

]