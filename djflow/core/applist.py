BEFORE_DJANGO_APPS = (

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
    'djflow.apps.flow',
    'djflow.apps.website',
    'djflow.apps.security',
)

THIRD_PARTY_APPS = (
    'solo',
)


INSTALLED_APPS = BEFORE_DJANGO_APPS + DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS
