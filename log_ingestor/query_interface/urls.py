import sys
sys.setrecursionlimit(1500) 

from django.contrib import admin
from django.urls import include, path
from log_ingestor.query_interface import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('log-ingestor/', include('log_app.urls')),
   
    # Add other URLs as needed
]
