from django.db import models
from django.contrib.auth.models import User


class ShortenedLink(models.Model):
    long_url = models.URLField(unique=True)
    short_key = models.CharField(max_length=10, unique=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='shortened_links', null=True)

    class Meta:
        verbose_name = 'Сокращённая ссылка'
        verbose_name_plural = 'Сокращённые ссылки'

    def get_short_url(self, request):
        return f"{request.scheme}://{request.get_host()}/{self.short_key}/"
