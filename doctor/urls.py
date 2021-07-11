from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('site_views.urls', namespace="Views")),
    path('user/', include('site_user.urls', namespace="User")),
    path('admin/', admin.site.urls),
]
