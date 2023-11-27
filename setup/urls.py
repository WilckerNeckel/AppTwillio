from django.contrib import admin
from django.urls import include, path
from ReceiveSms.views import TwilioWebhookView, SmsInfoListView
from rest_framework.authtoken import views 


urlpatterns = [
    path('smsmessages/', TwilioWebhookView.as_view(), name='smsmessages'),
    path('listmessages/', SmsInfoListView.as_view(), name='listmessages'),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
    path('admin/', admin.site.urls),
]


