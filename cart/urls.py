from django.urls import path
from . import views


urlpatterns = [
    path('total_amount', views.totalOrderValue, name='pay')
]
