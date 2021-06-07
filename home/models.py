from django.db import models
from uuid import uuid1


class UrlModel(models.Model):
    email = models.EmailField(500)
    original_url = models.URLField(500)
    summarized_url = models.UUIDField(default=uuid1, unique=True, editable=False)
