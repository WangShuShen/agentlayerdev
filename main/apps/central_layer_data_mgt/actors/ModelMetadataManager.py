"""
ModelMetadataManager actor
"""
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from main.utils.logger import log_trigger, log_writer

@csrf_exempt
@log_trigger("INFO")
def save_model_metadata(request):
    """
    save the model metadata
    """
    try:
        return HttpResponse("save_model_metadata finish")
    except Exception as e:
        log_writer('ERROR', save_model_metadata, (request,), message=e)
        return HttpResponse("save_model_metadata error")

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