from django.urls import path
from .views import (site_index)

app_name = 'Views'
urlpatterns = [
    path('', site_index, name="index_view"),
]
