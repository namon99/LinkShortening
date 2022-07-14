import random
import string
from django.db import IntegrityError
from django.http import HttpResponse
from django.views.generic import TemplateView

from .models import ShortenedLink


class MainPageView(TemplateView):
    template_name = 'general/main.html'

    def post(self, request, *args, **kwargs):
        long_url = request.POST['long_url']
        try:
            instance = ShortenedLink.objects.get(long_url=long_url)
            return HttpResponse(instance.get_short_url(request))
        except ShortenedLink.DoesNotExist:
            while True:
                short_key = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(6)])
                try:
                    instance = ShortenedLink.objects.create(long_url=long_url, short_key=short_key, user=request.user)
                except IntegrityError:
                    continue
                else:
                    return HttpResponse(instance.get_short_url(request))
