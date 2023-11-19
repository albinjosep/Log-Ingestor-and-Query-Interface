from django.contrib import admin
from django.urls import include, path
from query_interface.views import log_query
from .views import find_error_logs, search_logs, logs_for_resource, filter_logs_by_timestamp

# log_ingestor/urls.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('query-interface/', include('query_interface.urls')),
     path('log-ingestor/', include('log_app.urls', namespace='log_app')),
    path('query/', log_query, name='log_query'),
]


# Include URLs from log_app if applicable
# Adjust the path ('log-app/') and include statement based on your actual structure
urlpatterns += [
    path('log-app/', include('log_app.urls')),
    path('find-error-logs/', find_error_logs, name='find_error_logs'),
    path('search-logs/<str:term>/', search_logs, name='search_logs'),
    path('logs-for-resource/<str:resource_id>/', logs_for_resource, name='logs_for_resource'),
    path('filter-logs-by-timestamp/', filter_logs_by_timestamp, name='filter_logs_by_timestamp'),
]

# log_app/urls.py






