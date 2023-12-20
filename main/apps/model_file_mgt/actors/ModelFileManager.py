"""
ModelFileManager actor
"""
import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from main.utils.logger import log_trigger, log_writer

@csrf_exempt
# @log_trigger("INFO")
def save_model_file(request):
    """
    save the model file
    """
    if request.method == 'POST':
        try:
            # for one file
            model_name = request.POST.get('model_name')
            model_path = "main/apps/model_file_mgt/model_files/" + model_name
            with open(model_path, 'wb') as file:
                file.write(request.FILES['upload_file'].read())
            return HttpResponse("save_model_file finish")
        except Exception as e:
            log_writer('ERROR', save_model_file, (request,), message=e)
            return HttpResponse("save_model_file error")
    else:
        return JsonResponse({"error":"Invalid request method"})

@csrf_exempt
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

@csrf_exempt
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

@csrf_exempt
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