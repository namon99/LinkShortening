from django import template

from ..models import ShortenedLink


register = template.Library()


@register.simple_tag(takes_context=True)
def short_url(context, link: ShortenedLink):
    return link.get_short_url(context['request'])
