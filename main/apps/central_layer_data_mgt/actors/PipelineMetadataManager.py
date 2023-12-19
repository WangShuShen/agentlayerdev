"""
PipelineMetadataManager actor
"""
import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from main.utils.logger import log_trigger, log_writer
from ..models.training_pipeline import TrainingPipeline

@csrf_exempt
@log_trigger("INFO")
def save_pipeline_metadata(request):
    """
    save the pipeline metadata
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body).get("pipeline_metadata")
            for d in data:
                pipe_data = TrainingPipeline(
                    training_pipeline_uid = d["training_pipeline_uid"],
                    training_pipeline_created_time = d["training_pipeline_created_time"],
                    training_pipeline_name = d["training_pipeline_name"],
                    training_pipeline_description = d["training_pipeline_description"],
                    f_application_uid = d["application"]["application_uid"]
                )
                pipe_data.save()
            return HttpResponse("save_pipeline_metadata finish")
        except Exception as e:
            log_writer('ERROR', save_pipeline_metadata, (request,), message=e)
            return HttpResponse("save_pipeline_metadata error")
    else:
        return JsonResponse({"error":"Invalid request method"})

@csrf_exempt
@log_trigger("INFO")
def add_pipeline_metadata(request):
    """
    add the pipeline metadata
    """
    try:
        return HttpResponse("add_pipeline_metadata finish")
    except Exception as e:
        log_writer('ERROR', add_pipeline_metadata, (request,), message=e)
        return HttpResponse("add_pipeline_metadata error")

@csrf_exempt
@log_trigger("INFO")
def delete_pipeline_metadata(request):
    """
    delete the pipeline metadata
    """
    try:
        return HttpResponse("delete_pipeline_metadata finish")
    except Exception as e:
        log_writer('ERROR', delete_pipeline_metadata, (request,), message=e)
        return HttpResponse("delete_pipeline_metadata error")

@csrf_exempt 
@log_trigger("INFO")
def modify_pipeline_metadata(request):
    """
    modify the pipeline metadata
    """
    try:
        return HttpResponse("modify_pipeline_metadata finish")
    except Exception as e:
        log_writer('ERROR', modify_pipeline_metadata, (request,), message=e)
        return HttpResponse("modify_pipeline_metadata error")

@csrf_exempt 
@log_trigger("INFO")
def delete_all_pipeline_metadata(request):
    """
    delete all the pipeline metadata
    """
    try:
        return HttpResponse("delete_all_pipeline_metadata finish")
    except Exception as e:
        log_writer('ERROR', delete_all_pipeline_metadata, (request,), message=e)
        return HttpResponse("delete_all_pipeline_metadata error")
