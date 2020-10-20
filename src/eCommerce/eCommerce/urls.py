from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalogue.urls')),
    path('basket/', include('catalogue.urls'))
]
