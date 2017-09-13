import os

__PATH_MEDIA = os.path.dirname(os.path.dirname(__file__))

MEDIA_ROOT = os.path.join(__PATH_MEDIA, '../media/')
MEDIA_URL = '/media/'
