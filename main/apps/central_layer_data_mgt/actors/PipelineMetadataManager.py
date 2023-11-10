"""
PipelineMetadataManager actor
"""
from django.http import HttpResponse
from main.utils.logger import log_trigger, log_writer

@log_trigger("INFO")
def save_pipeline_metadata(request):
    """
    save the pipeline metadata
    """
    try:
        return HttpResponse("save_pipeline_metadata finish")
    except Exception as e:
        log_writer('ERROR', save_pipeline_metadata, (request,), message=e)
        return HttpResponse("save_pipeline_metadata error")

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
