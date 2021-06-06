from django.db import models


class UrlModel(models.Model):
    email = models.EmailField(500)
    original_url = models.URLField(500)
    summarized_url = models.UUIDField(unique=True)
