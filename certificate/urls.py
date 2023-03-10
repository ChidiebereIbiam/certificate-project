from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Kartexa"
admin.site.site_title = "Kartexa"
admin.site.index_title = "Kartexa"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls'))
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
