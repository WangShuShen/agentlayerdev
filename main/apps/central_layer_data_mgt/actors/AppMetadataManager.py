"""
AppMetadataManager actor
"""
import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from main.utils.logger import log_trigger, log_writer
from ..models.application import Application
import requests
@csrf_exempt
@log_trigger("INFO")
def save_application_metadata(request):
    """
    save the application metadata
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body).get("application_metadata")
            for d in data:
                app_data = Application(
                    application_uid = d["application_uid"],
                    application_created_time = d["application_created_time"],
                    application_description = d["application_description"],
                    application_name = d["application_name"]
                )
                app_data.save()
            return HttpResponse("save_application_metadata finish")
        except Exception as e:
            log_writer('ERROR', save_application_metadata, (request,), message=e)
            return HttpResponse("save_application_metadata error")
    else:
        return JsonResponse({"error":"Invalid request method"})

@csrf_exempt
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

@csrf_exempt
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

@csrf_exempt
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

@csrf_exempt
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
    
@csrf_exempt
@log_trigger("INFO")
def test_add_application_metadata(request):
    if request.method == 'POST':
        save_application_metadata_url = "https://6588786290fa4d3dabf9f644.mockapi.io/testapi"
        headers = {'Content-Type': 'application/json'}
        
        # 从外部API获取数据
        try:
            response = requests.post(save_application_metadata_url, headers=headers)
            response.raise_for_status()  # 检查响应状态
            data = response.json().get("application_metadata")
        except requests.RequestException as e:
            # 记录日志并返回错误信息
            log_writer('ERROR', "test_add_application_metadata", (request,), message=str(e))
            return HttpResponse("Error fetching data from external API")

        # 处理获取的数据
        try:
            for d in data:
                app_data = Application(
                    application_uid = d["application_uid"],
                    application_created_time = d["application_created_time"],
                    application_description = d["application_description"],
                    application_name = d["application_name"]
                )
                app_data.save()
            return HttpResponse("save_application_metadata finish")
        except Exception as e:
            log_writer('ERROR', "test_add_application_metadata", (request,), message=str(e))
            return HttpResponse("save_application_metadata error")
    else:
        return JsonResponse({"error": "Invalid request method"})