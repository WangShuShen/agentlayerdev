"""
DeployModelDataManager actor
"""
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from main.utils.logger import log_trigger, log_writer

@csrf_exempt
@log_trigger("INFO")
def add_positionid_data(request):
    """
    add position id data
    """
    try:
        return HttpResponse("add_positionid_data finish")
    except Exception as e:
        log_writer('ERROR', add_positionid_data, (request,), message=e)
        return HttpResponse("add_positionid_data error")

@csrf_exempt
@log_trigger("INFO")
def delete_positionid_data(request):
    """
    delete position id data
    """
    try:
        return HttpResponse("delete_positionid_data finish")
    except Exception as e:
        log_writer('ERROR', delete_positionid_data, (request,), message=e)
        return HttpResponse("delete_positionid_data error")

@csrf_exempt
@log_trigger("INFO")
def delete_all_positionid_data(request):
    """
    delete all position id data
    """
    try:
        return HttpResponse("delete_all_positionid_data finish")
    except Exception as e:
        log_writer('ERROR', delete_all_positionid_data, (request,), message=e)
        return HttpResponse("delete_all_positionid_data error")