from django.conf import settings

def get_settings(context):
    return {'SETTINGS': settings}
