from django.urls import path
from main.apps.central_layer_data_mgt.actors import AppMetadataManager

urlpatterns = [
    path('central_layer_data_mgt/AppMetadataManager/save_application_metadata', AppMetadataManager.save_application_metadata)
]