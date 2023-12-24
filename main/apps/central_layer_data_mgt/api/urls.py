from django.urls import path
from main.apps.central_layer_data_mgt.actors import AppMetadataManager, PipelineMetadataManager, ModelMetadataManager

import os
from dotenv import load_dotenv

central_layer_data_mgt = os.environ.get('HTTP_CENTRAL_LAYER_DATA_MGT_NAME')
urlpatterns = [
    path(f"{central_layer_data_mgt}/AppMetadataManager/test_add_application_metadata", AppMetadataManager.test_add_application_metadata),
    path(f"{central_layer_data_mgt}/AppMetadataManager/save_application_metadata", AppMetadataManager.save_application_metadata),
    path(f"{central_layer_data_mgt}/AppMetadataManager/add_application_metadata", AppMetadataManager.add_application_metadata),
    path(f"{central_layer_data_mgt}/AppMetadataManager/delete_application_metadata", AppMetadataManager.delete_application_metadata),
    path(f"{central_layer_data_mgt}/AppMetadataManager/modify_application_metadata", AppMetadataManager.modify_application_metadata),
    path(f"{central_layer_data_mgt}/AppMetadataManager/delete_all_application_metadata", AppMetadataManager.delete_all_application_metadata),
    path(f"{central_layer_data_mgt}/PipelineMetadataManager/save_pipeline_metadata", PipelineMetadataManager.save_pipeline_metadata),
    path(f"{central_layer_data_mgt}/PipelineMetadataManager/add_pipeline_metadata", PipelineMetadataManager.add_pipeline_metadata),
    path(f"{central_layer_data_mgt}/PipelineMetadataManager/delete_pipeline_metadata", PipelineMetadataManager.delete_pipeline_metadata),
    path(f"{central_layer_data_mgt}/PipelineMetadataManager/modify_pipeline_metadata", PipelineMetadataManager.modify_pipeline_metadata),
    path(f"{central_layer_data_mgt}/PipelineMetadataManager/delete_all_pipeline_metadata", PipelineMetadataManager.delete_all_pipeline_metadata),
    path(f"{central_layer_data_mgt}/ModelMetadataManager/save_model_metadata", ModelMetadataManager.save_model_metadata),
    path(f"{central_layer_data_mgt}/ModelMetadataManager/add_model_metadata", ModelMetadataManager.add_model_metadata),
    path(f"{central_layer_data_mgt}/ModelMetadataManager/delete_model_metadata", ModelMetadataManager.delete_model_metadata),
    path(f"{central_layer_data_mgt}/ModelMetadataManager/modify_model_metadata", ModelMetadataManager.modify_model_metadata),
    path(f"{central_layer_data_mgt}/ModelMetadataManager/delete_all_model_metadata", ModelMetadataManager.delete_all_model_metadata),
]