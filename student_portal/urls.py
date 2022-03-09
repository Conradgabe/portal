from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('portal.urls'), name='portal'),
    path('admin/', admin.site.urls),
]
