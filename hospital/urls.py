from django.contrib import admin
from django.urls import path, include
#  for images
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('users.urls')),
    path('patient/', include('patient.urls')),
    path('assistant/', include('assistant.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

admin.site.site_header = 'Hospital Administration'