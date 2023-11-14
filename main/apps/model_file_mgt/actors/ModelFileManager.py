"""
ModelFileManager actor
"""
from django.http import HttpResponse
from main.utils.logger import log_trigger, log_writer

@log_trigger("INFO")
def save_model_file(request):
    """
    save the model file
    """
    try:
        return HttpResponse("save_model_file finish")
    except Exception as e:
        log_writer('ERROR', save_model_file, (request,), message=e)
        return HttpResponse("save_model_file error")

@log_trigger("INFO")
def delete_model_file(request):
    """
    delete the model file
    """
    try:
        return HttpResponse("delete_model_file finish")
    except Exception as e:
        log_writer('ERROR', delete_model_file, (request,), message=e)
        return HttpResponse("delete_model_file error")

@log_trigger("INFO")
def send_model_file(request):
    """
    send the model file
    """
    try:
        return HttpResponse("send_model_file finish")
    except Exception as e:
        log_writer('ERROR', send_model_file, (request,), message=e)
        return HttpResponse("send_model_file error")

@log_trigger("INFO")
def delete_all_model_file(request):
    """
    delete all the model file
    """
    try:
        return HttpResponse("delete_all_model_file finish")
    except Exception as e:
        log_writer('ERROR', delete_all_model_file, (request,), message=e)
        return HttpResponse("delete_all_model_file error")