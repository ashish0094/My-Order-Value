from django.contrib import admin
from django.urls import path, include
from cart.views import totalOrderValue
urlpatterns = [
    path('admin/', admin.site.urls),
    path('totalordervalue/', include('cart.urls'))
]
