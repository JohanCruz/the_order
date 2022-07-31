from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('menu/<int:pk>/', views.menu_order, name='menu_order'),
    path('order/<int:pk>/', views.order, name='order'),
    path('processing/<int:pk>/', views.processing_orders, name='processing_orders'),
    path('change/status/<int:pk>/<str:status>/<int:restaurant>/', views.change_status, name='change_status'),
]