"""
CloseloopDataManager actor
"""
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from main.utils.logger import log_trigger, log_writer

@csrf_exempt
@log_trigger("INFO")
def add_closedloop_data(request):
    """
    add closedloop data
    """
    try:
        return HttpResponse("add_closedloop_data finish")
    except Exception as e:
        log_writer('ERROR', add_closedloop_data, (request,), message=e)
        return HttpResponse("add_closedloop_data error")

@csrf_exempt
@log_trigger("INFO")
def send_all_closedloop_data(request):
    """
    send all closedloop data
    """
    try:
        return HttpResponse("send_all_closedloop_data finish")
    except Exception as e:
        log_writer('ERROR', send_all_closedloop_data, (request,), message=e)
        return HttpResponse("send_all_closedloop_data error")