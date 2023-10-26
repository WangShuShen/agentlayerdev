from django.urls import path
from main.apps.data_mgt.actors import app_metadata_manager

urlpatterns = [
    path('app_metadata_manager/', app_metadata_manager.save_application_metadata)
]