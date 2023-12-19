"""
ModelMetadataManager actor
"""
import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from main.utils.logger import log_trigger, log_writer
from ..models.model import Model

@csrf_exempt
@log_trigger("INFO")
def save_model_metadata(request):
    """
    save the model metadata
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body).get("model_metadata")
            for d in data:
                model_data = Model(
                    model_uid = d["model_uid"],
                    model_created_time = d["model_created_time"],
                    model_version = d["model_version"],
                    model_file_path = d["model_file_path"],
                    model_file_extension = d["model_file_extension"],
                    model_access_token = d["model_access_token"],
                    model_description = d["model_description"],
                    model_published = d["model_published"],
                    f_training_pipeline_uid = d["training_pipeline"]["training_pipeline_uid"],
                    f_application_uid = d["application"]["application_uid"]
                )
                model_data.save()
            return HttpResponse("save_model_metadata finish")
        except Exception as e:
            log_writer('ERROR', save_model_metadata, (request,), message=e)
            return HttpResponse("save_model_metadata error")
    else:
        return JsonResponse({"error":"Invalid request method"})

@csrf_exempt
@log_trigger("INFO")
def add_model_metadata(request):
    """
    add the model metadata
    """
    try:
        return HttpResponse("add_model_metadata finish")
    except Exception as e:
        log_writer('ERROR', add_model_metadata, (request,), message=e)
        return HttpResponse("add_model_metadata error")

@csrf_exempt
@log_trigger("INFO")
def delete_model_metadata(request):
    """
    delete the model metadata
    """
    try:
        return HttpResponse("delete_model_metadata finish")
    except Exception as e:
        log_writer('ERROR', delete_model_metadata, (request,), message=e)
        return HttpResponse("delete_model_metadata error")

@csrf_exempt
@log_trigger("INFO")
def modify_model_metadata(request):
    """
    modify the model metadata
    """
    try:
        return HttpResponse("modify_model_metadata finish")
    except Exception as e:
        log_writer('ERROR', modify_model_metadata, (request,), message=e)
        return HttpResponse("modify_model_metadata error")

@csrf_exempt
@log_trigger("INFO")
def delete_all_model_metadata(request):
    """
    delete all the model metadata
    """
    try:
        return HttpResponse("delete_all_model_metadata finish")
    except Exception as e:
        log_writer('ERROR', delete_all_model_metadata, (request,), message=e)
        return HttpResponse("delete_all_model_metadata error")