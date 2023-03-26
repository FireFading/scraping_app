from django.db import models


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    link = models.CharField(max_length=2083, default="", verbose_name="Link")
    published = models.DateTimeField(verbose_name="Published at")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Parsed/created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")
    source = models.CharField(max_length=30, default="", blank=True, null=True, verbose_name="Source")

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
