from django import template
from django.core import urlresolvers
from django.contrib.contenttypes.models import ContentType


register = template.Library()


@register.inclusion_tag('edit_object_link.html')
def edit_link(obj):
    # via http://djangosnippets.org/snippets/1916/
    content_type = ContentType.objects.get_for_model(obj.__class__)
    return {'url': urlresolvers.reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=(obj.id,))}
