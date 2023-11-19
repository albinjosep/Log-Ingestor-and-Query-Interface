from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from log_ingestor import log_app
from .decorators import user_has_role
from log_ingestor.log_app.forms import LogSearchForm
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from log_ingestor.query_interface import views

from .models import Log, LogFile
from datetime import datetime

import json

import sys
sys.setrecursionlimit(1500) 

@csrf_exempt
def ingest_log(request):
    if request.method == 'POST':
        try:
            log_data = json.loads(request.body)
            Log.objects.create(**log_data)
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def log_query(request):
    pass


def find_error_logs(request):
    error_logs = Log.objects.filter(level='error')
    return render(request, 'error_logs.html', {'error_logs': error_logs})


def upload_log_file(log, file_data):
    file_name = f"{log.timestamp}_{log.id}.txt"  # Customize the file name as needed
    file_path = default_storage.save(file_name, ContentFile(file_data))
    LogFile.objects.create(log=log, file=file_path)

@user_has_role('admin')
def search_logs(request):
    form = LogSearchForm(request.GET)
    logs = Log.objects.all()

    if form.is_valid():
        logs = logs.filter(timestamp__gte=form.cleaned_data['start_date'])
        logs = logs.filter(timestamp__lte=form.cleaned_data['end_date'])
        logs = logs.filter(message__iregex=form.cleaned_data['regex_search'])
    if request.method == 'POST' and request.FILES.get('log_file'):
        log_file_data = request.FILES['log_file'].read()
        upload_log_file(log_app, log_file_data)
        # Add other filters

    return render(request, 'log_app/search_logs.html', {'form': form, 'logs': logs}) 
    
def logs_for_resource(request, resource_id):
    resource_logs = Log.objects.filter(resourceId=resource_id)
    return render(request, 'resource_logs.html', {'resource_logs': resource_logs})


def filter_logs_by_timestamp(request):
    start_timestamp = datetime(2023, 9, 10, 0, 0, 0)
    end_timestamp = datetime(2023, 9, 15, 23, 59, 59)
    timestamp_logs = Log.objects.filter(timestamp__range=(start_timestamp, end_timestamp))
    return render(request, 'timestamp_logs.html', {'timestamp_logs': timestamp_logs})






    

