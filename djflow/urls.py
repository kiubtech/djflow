from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from djflow.core.json_settings import get_settings

settings_json = get_settings()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('djflow.apps.website.urls')),
    url(r'^flow/', include('djflow.apps.flow.urls')),
    url(r'^security/', include('djflow.apps.security.urls'))
]

if settings_json["DEBUG"]:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
