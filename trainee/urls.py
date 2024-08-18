from django.urls import path
from .views import *

urlpatterns = [
    path("", trainees_list, name="trainees_list"),
    path("Add/", create_trainee, name="create_trainee"),
    path("Update/<int:id>/", update_trainee, name="update_trainee"),
    path("Delete/<int:id>/", delete_trainee, name="delete_trainee"),
    path("Details/<int:id>/", trainees_details, name="trainee_info"),
]
