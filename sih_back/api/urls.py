from django.urls import path

from sih_back.api.views import (
	entry_create_view,
	exit_create_view,
	access_log,
	emergency_view
)

app_name = "api"
urlpatterns = [
   path('entry/',entry_create_view,name="entry_create"),
   path('exit/',exit_create_view,name="exit_create"),
   path('access_log/',access_log,name="access_log"),
   path('emergency_message/',emergency_view,name="emergency_msg"),
]
