from django.urls import path
from main.apps.model_file_mgt.actors import ModelFileManager

urlpatterns = [
    path('model_file_mgt/ModelFileManager/save_model_file', ModelFileManager.save_model_file),
    path('model_file_mgt/ModelFileManager/delete_model_file', ModelFileManager.delete_model_file),
    path('model_file_mgt/ModelFileManager/send_model_file', ModelFileManager.send_model_file),
    path('model_file_mgt/ModelFileManager/delete_all_model_file', ModelFileManager.delete_all_model_file),
]