from django.db import models

from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool


class IconExtension(PageExtension):
    image = models.ImageField(upload_to='icons')
    a = models.CharField(max_length=10)

extension_pool.register(IconExtension)
