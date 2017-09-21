import os
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone
from tenant_schemas.utils import connection


class UserProfile(models.Model):

    def image_path(self, filename):
        extension = os.path.splitext(filename)[1][1:]
        file_name = os.path.splitext(filename)[0]
        url = "%s/Users/%s/profile/%s.%s" % (connection.tenant.domain_url, self.user.id, slugify(str(file_name)), extension)
        return url

    user = models.OneToOneField(User)
    image_profile = models.ImageField(upload_to=image_path, null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name()


# ============================================================
# Conectamos signals.
# ============================================================

from .signals import *

