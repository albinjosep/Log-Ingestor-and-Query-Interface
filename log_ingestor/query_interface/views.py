from django.shortcuts import render
from log_app.models import Log  # Import the Log model

def log_query(request):
    # Implement your log querying logic here
    logs = Log.objects.all()
    context = {'logs': logs}
    return render(request, 'query_interface/log_query.html', context)


