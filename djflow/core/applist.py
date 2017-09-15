BEFORE_DJANGO_APPS = (
    'tenant_schemas',
)

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.humanize',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

LOCAL_APPS = (
    'djflow.apps.tenant',
    'djflow.apps.flow',
    'djflow.apps.website',
    'djflow.apps.security',
)

THIRD_PARTY_APPS = (
    'solo',
)

SHARED_APPS = (
    'tenant_schemas',  # Siempre al inicio de todos.
    'djflow.apps.tenant',  # App donde reside nuestro modelo tenant.
    'djflow.apps.security',
    'djflow.apps.website',
    'django.contrib.contenttypes',
) + DJANGO_APPS


TENANT_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
) + LOCAL_APPS


INSTALLED_APPS = BEFORE_DJANGO_APPS + DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS
