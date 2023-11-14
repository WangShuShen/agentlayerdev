from django.urls import path
from main.apps.inference_layer_data_mgt.actors import RawDataManager, InferenceResultManager, ClosedloopDataManager
urlpatterns = [
    path('inference_layer_data_mgt/RawDataManager/add_raw_data', RawDataManager.add_raw_data),
    path('inference_layer_data_mgt/RawDataManager/send_all_raw_data', RawDataManager.send_all_raw_data),
    path('inference_layer_data_mgt/InferenceResultManager/add_inference_result', InferenceResultManager.add_inference_result),
    path('inference_layer_data_mgt/InferenceResultManager/send_all_inference_result', InferenceResultManager.send_all_inference_result),
    path('inference_layer_data_mgt/ClosedloopDataManager/add_closedloop_data', ClosedloopDataManager.add_closedloop_data),
    path('inference_layer_data_mgt/ClosedloopDataManager/send_all_closedloop_data', ClosedloopDataManager.send_all_closedloop_data),
]