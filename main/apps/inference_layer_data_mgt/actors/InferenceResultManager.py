"""
InferenceResultManager actor
"""
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from main.utils.logger import log_trigger, log_writer

@csrf_exempt
@log_trigger("INFO")
def add_inference_result(request):
    """
    add inference result
    """
    try:
        return HttpResponse("add_inference_result finish")
    except Exception as e:
        log_writer('ERROR', add_inference_result, (request,), message=e)
        return HttpResponse("add_inference_result error")

@csrf_exempt
@log_trigger("INFO")
def send_all_inference_result(request):
    """
    send all inference result
    """
    try:
        return HttpResponse("send_all_inference_result finish")
    except Exception as e:
        log_writer('ERROR', send_all_inference_result, (request,), message=e)
        return HttpResponse("send_all_inference_result error")