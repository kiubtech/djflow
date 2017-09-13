from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import SiteConfiguration

admin.site.register(SiteConfiguration, SingletonModelAdmin)
