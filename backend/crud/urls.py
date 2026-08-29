from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework.routers import  DefaultRouter

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#router = DefaultRouter()
#router.register('', --ViewSet, basename='')

#urlpatterns = router.urls