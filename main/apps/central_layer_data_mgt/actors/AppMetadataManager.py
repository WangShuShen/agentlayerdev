"""
AppMetadataManager actor
"""
from django.http import HttpResponse
from main.utils.logger import log_trigger, log_writer

@log_trigger("INFO")
def save_application_metadata(request):
    """
    save the application metadata
    """
    try:
        return HttpResponse("save_application_metadata finish")
    except Exception as e:
        log_writer('ERROR', save_application_metadata, (request,), message=e)
        return HttpResponse("save_application_metadata error")

@log_trigger("INFO")
def add_application_metadata(request):
    """
    add the application metadata
    """
    try:
        return HttpResponse("add_application_metadata finish")
    except Exception as e:
        log_writer('ERROR', add_application_metadata, (request,), message=e)
        return HttpResponse("add_application_metadata error")

@log_trigger("INFO")
def delete_application_metadata(request):
    """
    delete the application metadata
    """
    try:
        return HttpResponse("delete_application_metadata finish")
    except Exception as e:
        log_writer('ERROR', delete_application_metadata, (request,), message=e)
        return HttpResponse("delete_application_metadata error")

@log_trigger("INFO")
def modify_application_metadata(request):
    """
    modify the application metadata
    """
    try:
        return HttpResponse("modify_application_metadata finish")
    except Exception as e:
        log_writer('ERROR', modify_application_metadata, (request,), message=e)
        return HttpResponse("modify_application_metadata error")

@log_trigger("INFO")
def delete_all_application_metadata(request):
    """
    delete all the application metadata
    """
    try:
        return HttpResponse("delete_all_application_metadata finish")
    except Exception as e:
        log_writer('ERROR', delete_all_application_metadata, (request,), message=e)
        return HttpResponse("delete_all_application_metadata error")