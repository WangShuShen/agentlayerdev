"""
RawDataManager actor
"""
from django.http import HttpResponse
from main.utils.logger import log_trigger, log_writer

@log_trigger("INFO")
def add_raw_data(request):
    """
    add raw data
    """
    try:
        return HttpResponse("add_raw_data finish")
    except Exception as e:
        log_writer('ERROR', add_raw_data, (request,), message=e)
        return HttpResponse("add_raw_data error")

@log_trigger("INFO")
def send_all_raw_data(request):
    """
    send all raw data
    """
    try:
        return HttpResponse("send_all_raw_data finish")
    except Exception as e:
        log_writer('ERROR', send_all_raw_data, (request,), message=e)
        return HttpResponse("send_all_raw_data error")