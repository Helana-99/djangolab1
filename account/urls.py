from django.urls import path
from .views import *

urlpatterns = [
    path('', account_list, name='account_list'),
    path('Add/', create_account, name='create_account'),
    path('Update/<int:id>/', update_account, name='update_account'),
    path('Delete/<int:id>/', delete_account, name='delete_account'),
    path('Info/<int:id>/', account_info, name='account_info'),
]
