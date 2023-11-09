from django.urls import path
from main.apps.central_layer_data_mgt.actors import AppMetadataManager

urlpatterns = [
    path('central_layer_data_mgt/AppMetadataManager/save_application_metadata', AppMetadataManager.save_application_metadata),
    path('central_layer_data_mgt/AppMetadataManager/add_application_metadata', AppMetadataManager.add_application_metadata),
    path('central_layer_data_mgt/AppMetadataManager/delete_application_metadata', AppMetadataManager.delete_application_metadata),
    path('central_layer_data_mgt/AppMetadataManager/modify_application_metadata', AppMetadataManager.modify_application_metadata)
]