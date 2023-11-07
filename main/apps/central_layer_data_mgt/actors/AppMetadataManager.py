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