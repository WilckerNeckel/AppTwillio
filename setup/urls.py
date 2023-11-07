from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from ReceiveSms.views import TwilioWebhookView
from rest_framework.authtoken import views 

router = routers.DefaultRouter()
router.register(r'smsmessages', TwilioWebhookView, basename='Messages')


urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token, name='api-tokn-auth'), 
    path('admin/', admin.site.urls),
]


