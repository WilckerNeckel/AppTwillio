
from django.contrib import admin
from django.urls import path
from ReceiveSms.views import ReceiveSms

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ReceiveSms', ReceiveSms)
]
